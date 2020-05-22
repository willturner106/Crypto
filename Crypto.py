#Will Turner 2020

import re
import warnings
import math


class ADFGVX:

    plain = ""
    cipher = ""
    keyword = ""
    matrix = ""

    def __init__(self, plain="",cipher="",keyword="",matrix="",matrixString=""):
        self.plain = plain
        self.cipher = cipher
        self.keyword = keyword
        if(matrixString != ""):
            matrixString = list(matrixString)
            self.matrix = [''] * 6
            for i in range(6):
                self.matrix[i] = matrixString[i * 6:i * 6 + 6]
        else:
            self.matrix = matrix
        #if self.plain != "":
            #self.prepare

    def encode(self):  #  , matrixString, keyword, plaintext):
        matrix = self.matrix
        keyword = self.keyword
        plaintext = self.plain
        p = plaintext

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        ct = ""

        #Substitution
        for item in list(p):
            for i in range(len(matrix)):
                if item in matrix[i]:
                    column = matrix[i].index(item)
                    row = i
            ct += list("ADFGVX")[row]
            ct += list("ADFGVX")[column]

        # Transpose
        t = ColumnarTransposition(plain=ct, keyword=keyword)
        ct = t.encode()
        ctList = [ct[i:i + 2] for i in range(0, len(ct), 2)]
        ct = " ".join(ctList)

        #print("Done Encoding")
        self.cipher = ct
        return ct

    def prepare_string(s):
        s = re.sub(r'[^\w\s]', "", s)
        s = re.sub(re.compile(r'\s+'), '', s)
        return s.upper()

    def switchRow(l, a, b):
        for i in range(len(l)):
            ADFGVX.switch(l[i], int(a), int(b))
        return l

    def switch(l, a, b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp

    def decode(self):#matrixString, keyword, ciphertext):

        matrix = self.matrix
        keyword = self.keyword
        ciphertext = self.cipher

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        ciphertext = ciphertext.replace(" ","")
        t = ColumnarTransposition(cipher=ciphertext,keyword=keyword)
        pl = t.decode()


        #print("ADFGVX matrix:")
        #for item in matrix:
            #print(item)

        ctList = [pl[i:i + 2] for i in range(0, len(pl), 2)]
        ct = ""

        for item in ctList:
            row = list("ADFGVX").index(list(item)[0])
            column = list("ADFGVX").index(list(item)[1])
            ct += matrix[row][column]

        return ct


class Affine:

    plain = ""
    cipher = ""
    a = ""
    b = ""
    alpha = ""
    mod = 0

    def __init__(self, plain="", cipher="", a="", b="",alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.plain = plain
        self.cipher = cipher
        self.a = a
        self.b = b
        self.alpha = alpha
        self.mod = len(alpha)

    def i2c(self, i, ALPHABET):
        return ALPHABET[i]

    def c2i(self, c, ALPHABET):
        return ALPHABET.find(c)

    def prepare_string(self, s):
        s = re.sub(r'[^\w\s]', "", s)
        s = re.sub(re.compile(r'\s+'), '', s)
        return s.upper()

    def mod_inverse(self, a, m):
        for i in range(m):
            if (i * a % m == 1):
                return i
        raise ValueError("No multiplicative inverse of a within mod m")

    def encode(self):  #, plaintext, alphabet, a, b):
        mod = len(self.alpha)
        cipher = ""
        for item in list(self.plain):
            cipher += self.i2c(((self.c2i(item, self.alpha) * self.a) + self.b) % mod, self.alpha)
        self.cipher = cipher
        return cipher

    def decode(self):  #, ciphertext, alphabet, a, b):
        mod = len(self.alpha)
        plain = ""
        a1 = self.mod_inverse(self.a, len(self.alpha))
        for item in list(self.cipher):
            plain += self.i2c(a1 * (self.c2i(item, self.alpha) - self.b) % mod, self.alpha)
        self.plain = plain
        return plain


class Atbash(Affine):

    # Atbash is Affine where a = b = (m-1)
    def __init__(self, plain="", cipher="", alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        Affine.__init__(self, plain=plain, cipher=cipher, a=(len(alpha)-1), b=(len(alpha)-1), alpha=alpha)


class Hill:

    keyMatrix = ""
    invMatrix = ""
    cipher = ""
    plain = ""
    alpha = ""
    mod = ""

    def __init__(self, plain="", cipher="", key="", keyMatrix = "", invMatrix="", alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.plain = plain
        self.cipher = cipher
        self.alpha = alpha
        self.mod = len(self.alpha)
        if(keyMatrix != ""):
            self.keyMatrix = keyMatrix
        elif key != "":
            self.keyMatrix = self.getKeyMatrix(key)
        if(invMatrix != ""):
            self.invMatrix = invMatrix
        elif key != "":
            self.invMatrix = self.inverseKey(key)


    def getKeyMatrix(self, key):
        keyMatrix = [[0] * 2 for i in range(2)]
        key = key.split()
        k = 0
        for i in range(2):
            for j in range(2):
                keyMatrix[i][j] = int(key[k])
                k += 1
        return keyMatrix

    def inverseKey(self, key):  #, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        alpha = self.alpha
        mod = self.mod
        k = self.getKeyMatrix(key)
        d = ((k[0][0] * k[1][1]) - (k[0][1] * k[1][0]))
        d = self.mod_inverse(d, mod)
        invMatrix = [[k[1][1], k[0][1] * -1], [k[1][0] * -1, k[0][0]]]

        for i in range(len(invMatrix)):
            for l in range(len(invMatrix[0])):
                invMatrix[i][l] = invMatrix[i][l] * d % mod

        return invMatrix

    def mod_inverse(self, a, m):
        for i in range(m):
            if (i * a % m == 1):
                return i

    # Following function encrypts the message
    def vencode(self, messageMatrix, keyMatrix, alpha):
        mod = len(alpha)
        cipherMatrix = [0] * (len(messageMatrix))
        for i in range(len(cipherMatrix)):
            cipherMatrix[i] = [0] * 2
        for i in range(len(messageMatrix)):
            for j in range(2):
                cipherMatrix[i][j] = 0
                for x in range(2):
                    cipherMatrix[i][j] += (keyMatrix[j][x] * messageMatrix[i][x])
                cipherMatrix[i][j] = cipherMatrix[i][j] % mod
        return cipherMatrix

    def decode(self):  #cipher, key, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        t = self.HillCipher(self.cipher, self.invMatrix, self.alpha)
        self.plain = t
        return t

    def encode(self):  #plain, key, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        t = self.HillCipher(self.plain, self.keyMatrix, self.alpha)
        self.cipher = t
        return t

    def HillCipher(self, message, keyMatrix, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        # Get key matrix from the key string

        # Generate vector for the message
        messageVector = [0] * (len(message) // 2)
        for i in range(len(messageVector)):
            messageVector[i] = [0] * 2
        c = 0
        for l in range(len(message) // 2):
            for i in range(2):
                messageVector[l][i] = alpha.find(message[c])
                c += 1

        # Following function generates
        # the encrypted vector
        cipherMatrix = self.vencode(messageVector, keyMatrix, alpha)

        # Generate the encrypted text
        # from the encrypted vector
        CipherText = []
        for j in range(len(cipherMatrix)):
            for i in range(2):
                CipherText.append(alpha[cipherMatrix[j][i]])

                # Finally print the ciphertext
        return "".join(CipherText)


class Morse:

    plain = ""
    cipher = ""
    mdict = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
    }

    def __init__(self, plain="", cipher=""):
        self.plain = plain
        self.cipher = cipher

    def encode(self):
        ret = ""
        for i in self.plain:
            if i in self.mdict.keys():
                ret += self.mdict[i] + " "
            elif i.swapcase() in self.mdict.keys():
                ret += self.mdict[i.swapcase()] + " "
        self.cipher = ret
        return ret

    def decode(self):
        ret = ""
        inv_map = {v: k for k, v in self.mdict.items()}
        for i in self.cipher.split(" "):
            if i in inv_map.keys():
                ret += inv_map[i]
        self.cipher = ret
        return ret


class Playfair:

    plain = ""
    cipher = ""
    grid = ""
    ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def __init__(self, plain="", cipher="", keyword="", grid=""):
        self.plain = plain
        self.cipher = cipher
        if keyword != "":
            self.grid = self.makeGrid(keyword)
        else:
            self.grid = grid

    # TODO: PLayfair encode method

    def decode(self):  #, string, word):
        #grid = self.makeGrid(word)
        # for item in grid:
        #  print(item)
        t = self.decodeWithGrid(self.cipher, self.grid)
        self.plain = t
        return t

    def decodeWithGrid(self, string, grid):
        plain = ""

        cipher = string.split(" ")

        for item in cipher:
            first = self.getLocation(list(item)[0], grid)
            second = self.getLocation(list(item)[1], grid)

            # 3 cases, same row, same column, neither
            if (first[0] == second[0]):
                plain += grid[first[0]][first[1] - 1]
                plain += grid[second[0]][second[1] - 1]
            elif (first[1] == second[1]):
                plain += grid[first[0] - 1][first[1]]
                plain += grid[second[0] - 1][second[1]]
            else:
                plain += grid[first[0]][second[1]]
                plain += grid[second[0]][first[1]]

        return plain

    def makeGrid(self, word):
        word = word.replace("J", "")
        grid = [''] * 5
        for x in range(len(grid)):
            grid[x] = [''] * 5

        string = ""

        for item in word:
            if not item in string:
                string += item
        for item in self.ALPHABET:
            if not item in string:
                string += item

        string = list(string)
        count = 0
        for i in range(len(grid)):
            for l in range(len(grid[0])):
                grid[i][l] = string[count]
                count += 1
        return grid

    def getLocation(self, letter, grid):
        for i in range(len(grid)):
            for l in range(len(grid[i])):
                if (grid[i][l] == letter):
                    return (i, l)


class RailFence:

    cipher = ""
    plain = ""
    rows = 3

    def __init__(self, plain="", cipher="", rows=3, removeSpaces=True, capitalize=True):
        self.cipher = cipher
        self.plain = plain
        self.rows = rows
        if removeSpaces:
            self.plain = self.plain.replace(" ","")
            self.cipher = self.cipher.replace(" ","")
        if capitalize:
            self.plain = self.plain.upper()
            self.cipher = self.cipher.upper()

    def encode(self):
        plain_text = self.plain
        # divide plain text into layers number of strings
        rail = [""] * self.rows
        layer = 0
        adding = True
        for character in plain_text:
            rail[layer] += character
            if layer >= self.rows - 1 or not adding:
                layer -= 1
                adding = False
                if layer == 0:
                    adding = True
            else:
                layer += 1

        cipher = "".join(rail)
        self.cipher = cipher
        return cipher

    def decode(self):
        numrails = self.rows
        text = self.cipher
        rng = range(len(text))
        fence = [[None] * len(rng) for n in range(numrails)]
        rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
        for n, x in enumerate(rng):
            fence[rails[n % len(rails)]][n] = x
        pos = [c for rail in fence for c in rail if c is not None]
        self.plain = ''.join(text[pos.index(n)] for n in rng)
        return ''.join(text[pos.index(n)] for n in rng)


class ColumnarTransposition:

    plain = ""
    cipher = ""
    key = ""

    def __init__(self, plain="", cipher="", key="", keyword=""):
        self.plain = plain
        self.cipher = cipher
        self.key = key
        self.keyword = self.checkKeyword(keyword)
        print(self.keyword)

    def checkKeyword(self, keyword):
        return "".join(dict.fromkeys(keyword))

    def decode(self):  # , cipher, key):
        """
        Decode a transposition-encyphered string

        :param str cipher: The string to be decoded
        :param int key: The number of columns used to encode
        :return: The decoded string
        """
        if(self.key != ""):
            return self.decryptTranspose(self.cipher, self.key)
        return self.keyWord(self.cipher, self.keyword)

    def encode(self):  # plain, key):
        """
        Encode a string using a transposition cipher

        :param str plain: The plaintext to be encoded
        :param int key: The number of columns used to encode
        :return: The encoded string
        """
        if(self.key != ""):
            return self.transpose(self.plain, self.key)
        return self.encodeWithKeyword(self.plain, self.keyword)

    def transpose(self, plain, key):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(plain):
                ciphertext[col] += plain[pointer]
                pointer += key
        print(ciphertext)
        self.cipher = ''.join(ciphertext)
        return ''.join(ciphertext)

    def decryptTranspose(self, cipher, key):

        if (not len(cipher) % key == 0):
            if (key - (len(cipher) % key) == 1):
                cipher += 'X'
            else:
                num = key - (len(cipher) % key)
                for i in range(num):
                    temp = list(cipher)
                    p = len(cipher) - (((len(cipher) // key) + 1) * i)
                    temp = temp[0:p] + ['X'] + temp[p:]
                    cipher = ''.join(temp)
            # print(cipher)

        leng = len(cipher)
        matrix = [] * key
        for i in range(leng // key):
            matrix.append([''] * key)
        cipherList = list(cipher)

        count = 0

        for i in range(key):
            for l in range(leng // key):
                matrix[l][i] = cipherList[count]
                count += 1
        output = ""
        for item in matrix:
            # print(item)
            for l in item:
                output += l
        self.plain = output
        return output

    def encodeWithKeyword(self, plain, word):
        key = len(word)
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(plain):
                ciphertext[col] += plain[pointer]
                pointer += key

        ret = ""
        store = word
        word = list(word)
        word.sort()
        for item in word:
            num = store.find(item)
            ret += ciphertext[num]


        self.cipher =ret
        return ret

    def keyWord(self, cipher, word):
        """Decrypts with a keyword"""
        key = len(word)

        #Add ~ to make the length right
        if (not len(cipher) % key == 0):
            num = key - (len(cipher) % key)
            w = list(word)
            w.sort()
            xspots = []
            for i in range(num):
                xspots.append(w.index(word[len(word)-i-1]))
            xspots.sort()
            for xPos in xspots:
                temp = list(cipher)
                p = (math.ceil(len(cipher) / key) * xPos) + math.ceil(len(cipher) / key)
                temp = temp[0:p-1] + ['~'] + temp[p-1:]
                cipher = ''.join(temp)

        #Create matrix
        leng = len(cipher)
        matrix = [] * key
        for i in range(leng // key):
            matrix.append([''] * key)
        cipherList = list(cipher)

        count = 0

        #add to matrix
        for i in range(key):
            for l in range(leng // key):
                matrix[l][i] = cipherList[count]
                count += 1

        word = list(word)
        og = list(word)
        # print("\n")
        word.sort()
        # print(word)

        word = list(word)
        # print("\n")
        for i in range(10):
            for l in range(len(word) - 1):
                if (og.index(word[l]) > og.index(word[l + 1])):
                    word[l], word[l + 1] = word[l + 1], word[l]
                    for i in range(len(matrix)):
                        self.switch(matrix[i], l, l + 1)

        output = ""
        for item in matrix:
            for l in item:
                output += l

        self.plain = output.replace("~","")
        return output.replace("~","")

    def switchRow(self, l, a, b):
        for i in range(len(l)):
            self.switch(l[i], int(a), int(b))
        return l

    def switch(self, l, a, b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp


class Caesar(Affine):  # Caesar cipher is just an Affine cipher where a=1 and b = shift

    def __init__(self, plain="", cipher="", shift=1, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        Affine.__init__(self, plain=plain, cipher=cipher, a=1, b=shift, alpha=alpha)


class SubCipher:

    plain = ""
    cipher = ""
    plainAlpha = ""
    cipherAlpha = ""

    def __init__(self, plain="", cipher="", plainAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ", cipherAlpha=""):
        self.plain = plain
        self.cipher = cipher
        self.plainAlpha = plainAlpha
        self.cipherAlpha = cipherAlpha
        if not self.subst_validate(plainAlpha, cipherAlpha):
            print("Alphabets do not match")

    def subst_validate(self, alpha1, alpha2):
        if not len(alpha1) == len(alpha2):
            warnings.warn("Alphabet lengths do not match")
            return False
        for i in alpha1:
            if i not in alpha2:
                warnings.warn("Alphabets do not contain the same character sets")  # TODO make this warning clearer
                return False
        return True

    def encode(self):

        s = list(self.plain)

        a1 = list(self.plainAlpha)
        a2 = list(self.cipherAlpha)

        for i in range(len(s)):
            if s[i].upper() in a2:
                if s[i].isupper():
                    s[i] = a2[a1.index(s[i])]
                else:
                    s[i] = a2[a1.index(s[i].upper())].lower()

        self.cipher = "".join(s)
        return "".join(s)

    def decode(self):
        s = list(self.cipher)

        a1 = list(self.plainAlpha)
        a2 = list(self.cipherAlpha)

        for i in range(len(s)):
            if s[i].upper() in a2:
                if s[i].isupper():
                    s[i] = a1[a2.index(s[i])]
                else:
                    s[i] = a1[a2.index(s[i].upper())].lower()

        self.plain = "".join(s)
        return "".join(s)


class Vigenere:

    alpha = ""
    plain = ""
    cipher = ""
    keyword = ""

    def __init__(self, plain="", cipher="", keyword="", alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.plain = plain
        self.cipher = cipher
        self.keyword = keyword
        self.alpha = alpha

    def encode(self):

        keyword = self.keyword
        alpha = self.alpha

        cipher = ""
        k = list(keyword)
        count = 0

        for item in list(self.plain):
            cipher += alpha[(alpha.find(item) + alpha.find(k[count])) % 26]
            count += 1
            if count >= len(keyword):
                count = 0

        self.cipher = cipher
        return cipher

    def decode(self):

        keyword = self.keyword
        alpha = self.alpha

        cipher = ""
        k = list(keyword)
        count = 0

        for item in list(self.cipher):
            cipher += alpha[(alpha.find(item) - alpha.find(k[count])) % 26]
            count += 1
            if (count >= len(keyword)):
                count = 0

        self.plain = cipher
        return cipher

r = RailFence(plain="gotta test with multiple rail lengths", rows=7)
print(r.encode())
print(r.decode())