#Will Turner 2020

import re
import random


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

    def encode(self):  #  , matrixString, keyword, plaintext):
        matrix = self.matrix
        keyword = self.keyword
        plaintext = self.plain
        p = plaintext

        """
        ran = input("Random matrix? (y/n)")
        if (ran == "y" or ran == "Y"):
            matrixString = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
            random.shuffle(matrixString)
            matrixString = "".join(matrixString)
        """

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        """
        if (not len(matrixString) == 36):
            return "ERROR: Matrix not 36 characters"
        for item in list(alpha):
            if (not item in matrixString):
                return "ERROR: Matrix missing letter '" + item + "'"


        p = ADFGVX.prepare_string(plaintext)
        matrixString = list(matrixString)
        ct = ""
        matrix = [''] * 6

        for i in range(6):
            matrix[i] = matrixString[i * 6:i * 6 + 6]
        """
        ct = ""

        #print("ADFGVX matrix:")
        #for item in matrix:
            #print(item)

        for item in list(p):
            for i in range(len(matrix)):
                if item in matrix[i]:
                    column = matrix[i].index(item)
                    row = i
            ct += list("ADFGVX")[row]
            ct += list("ADFGVX")[column]

        # print("Transposing")
        ct = self.transposeEncode(ct, keyword)
        ctList = [ct[i:i + 2] for i in range(0, len(ct), 2)]

        ct = ""
        for i in ctList:
            ct += i
            ct += " "

        #print("Done Encoding")
        self.cipher = ct
        return ct

    def prepare_string(s):
        s = re.sub(r'[^\w\s]', "", s)
        s = re.sub(re.compile(r'\s+'), '', s)
        return s.upper()

    def transposeEncode(self, string, keyword):
        #print(string)
        ct = ""
        numColumns = len(keyword)
        numColumns = len(string) // len(keyword)
        numRows = len(string) // numColumns
        numRows = len(keyword)
        if (not len(string) % numRows == 0):
            numColumns += 1

        matrix = [''] * numColumns
        for i in range(len(matrix)):
            matrix[i] = [''] * numRows
        row = 0
        col = 0
        for item in list(string):
            matrix[row][col] = item
            col += 1
            if (col >= numRows):
                col = 0
                row += 1
        #for item in matrix:
            #print(item)
        ak = list(keyword)
        ak.sort()

        for item in ak:
            num = list(keyword).index(item)
            for i in range(len(matrix)):
                ct += "".join(matrix[i][num])

        # print("Transposition matrix:")
        # for item in matrix:
        #  print (item)

        return ct

    def transposeDecode(self, cipher, word):
        key = len(word)

        numBlanks = len(word) - (len(cipher) % len(word))

        leng = len(cipher)
        matrix = [] * key
        for i in range(leng // key + 1):
            matrix.append([''] * key)

        sWord = list(word)
        sWord.sort()
        for i in range(numBlanks):
            matrix[len(matrix) - 1][word.index(sWord[len(sWord) - i - 1])] = ":"

        cipherList = list(cipher)

        count = 0
        #print(cipher)
        for i in range(key):
            for l in range(leng // key + 1):
                if (matrix[l][i] != ":"):
                    matrix[l][i] = cipherList[count]
                    count += 1
        #for item in matrix:
            #print(item)

        word = list(word)
        og = list(word)
        for i in range(10):
            for l in range(len(word) - 1):
                if (word[l] > word[l + 1]):
                    word[l], word[l + 1] = word[l + 1], word[l]

        word = list(word)
        for i in range(10):
            for l in range(len(word) - 1):
                if (og.index(word[l]) > og.index(word[l + 1])):
                    word[l], word[l + 1] = word[l + 1], word[l]
                    for i in range(len(matrix)):
                        ADFGVX.switch(matrix[i], l, l + 1)

        output = ""
        for item in matrix:
            for l in item:
                output += l
        #print(output)
        return output.replace(":", "")

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
        """
        if (not len(matrixString) == 36):
            return "ERROR: Matrix not 36 characters"
        for item in list(alpha):
            if (not item in matrixString):
                return "ERROR: Matrix missing letter '" + item + "'"

        ciphertext = ADFGVX.prepare_string(ciphertext)
        """

        ciphertext = ciphertext.replace(" ","")
        pl = self.transposeDecode(ciphertext, keyword)

        """
        matrixString = list(matrixString)
        matrix = [''] * 6

        for i in range(6):
            matrix[i] = matrixString[i * 6:i * 6 + 6]
        """

        #print("ADFGVX matrix:")
        #for item in matrix:
            #print(item)

        ctList = [pl[i:i + 2] for i in range(0, len(pl), 2)]
        #print(pl,ctList)
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
        else:
            self.keyMatrix = self.getKeyMatrix(key)
        if(invMatrix != ""):
            self.invMatrix = invMatrix
        else:
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


class ColumnarTransposition:

    plain = ""
    cipher = ""
    key = ""

    def __init__(self, plain="", cipher="", key=""):
        self.plain = plain
        self.cipher = cipher
        self.key = key

    def decode(self):  # , cipher, key):
        """
        Decode a transposition-encyphered string

        :param str cipher: The string to be decoded
        :param int key: The number of columns used to encode
        :return: The decoded string
        """
        return self.decryptTranspose(self.cipher, self.key)

    def encode(self):  # plain, key):
        """
        Encode a string using a transposition cipher

        :param str plain: The plaintext to be encoded
        :param int key: The number of columns used to encode
        :return: The encoded string
        """
        return self.transpose(self.plain, self.key)

    def transpose(self, plain, key):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(plain):
                ciphertext[col] += plain[pointer]
                pointer += key
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

    def keyWord(self, cipher, word):
        """Decrypts with a keyword"""

        key = len(word)
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
        # print(list(word))
        # for item in matrix:
        # print(item)

        word = list(word)
        og = list(word)
        # print("\n")
        for i in range(10):
            for l in range(len(word) - 1):
                if (word[l] > word[l + 1]):
                    word[l], word[l + 1] = word[l + 1], word[l]
        # print(word)

        word = list(word)
        # print("\n")
        for i in range(10):
            for l in range(len(word) - 1):
                if (og.index(word[l]) > og.index(word[l + 1])):
                    word[l], word[l + 1] = word[l + 1], word[l]
                    for i in range(len(matrix)):
                        self.switch(matrix[i], l, l + 1)

        # print(word)
        output = ""
        for item in matrix:
            # print(item)
            for l in item:
                output += l

        return output

    def switchRow(self, l, a, b):
        for i in range(len(l)):
            self.switch(l[i], int(a), int(b))
        return l

    def switch(self, l, a, b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp


#a = ADFGVX(plain="THISISAMESSAGEOFADIFFERENTLENGTH", keyword="UHKEY", matrixString="8QXEPM9AK6T3VG52HCIDBJZ4RSU1LWO0FYN7" )
#print(a.encode())
#print(a.decode())

