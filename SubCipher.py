# Will Turner 2020

import re
from collections import Counter

# Will Turner, 2/6/2020
# All ciphers preserve case, spacing, and punctuation
# All encoding and decoding methods are in the subCipher class
# All cracking tools are in the crackingTools class

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]

manyWords = open('WordLists/morewords.txt', 'r').readlines()
manyWords = [manyWords[x][0:len(manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(manyWords) - 1)]


class subCipher:

    def c2i(c, alphabet):
        return alphabet.index(c)

    def i2c(i, alphabet):
        return list(alphabet)[i]

    def prepareString(s):
        s = re.sub(r'[^\w\s]', "", s)
        s = re.sub(re.compile(r'\s+'), '', s)
        return s.upper()

    def caesar_shift_encode(p, s, a):
        result = ""
        a1 = a.upper()
        a2 = a.lower()
        for i in range(len(p)):
            char = p[i]
            if (char in a1):
                result += subCipher.i2c((subCipher.c2i(char, a1) + s) % len(a1), a1)
            elif (char in a2):
                result += subCipher.i2c((subCipher.c2i(char, a2) + s) % len(a2), a2)
            else:
                result += char
        return result

    def caesar_shift_decode(p, s, a):
        result = ""
        a1 = a.upper()
        a2 = a.lower()
        for i in range(len(p)):
            char = p[i]
            if (char in a1):
                result += subCipher.i2c((subCipher.c2i(char, a1) - s) % len(a1), a1)
            elif (char in a2):
                result += subCipher.i2c((subCipher.c2i(char, a2) - s) % len(a2), a2)
            else:
                result += char
        return result

    def subst_validate(alpha1, alpha2):
        if (not len(alpha1) == len(alpha2)):
            return False
        for i in alpha1:
            if (not i in alpha2):
                return False
        return True

    def substitution_cipher_encode(s, a1, a2):
        s = list(s)

        if (not subCipher.subst_validate(a1, a2)):
            print("Uhh Oh! The alphabets don't match!")
            return

        a1 = list(a1)
        a2 = list(a2)

        for i in range(len(s)):
            if (s[i].upper() in a2):
                if (s[i].isupper()):
                    s[i] = a2[a1.index(s[i])]
                else:
                    s[i] = a2[a1.index(s[i].upper())].lower()

        return "".join(s)

    def substitution_cipher_decode(s, a1, a2):
        s = list(s)
        # if(not subCipher.subst_validate(a1,a2)):
        # print("Uhh Oh! The alphabets don't match!")
        # return
        a1 = list(a1)
        a2 = list(a2)

        for i in range(len(s)):
            if (s[i].upper() in a2):
                if (s[i].isupper()):
                    s[i] = a1[a2.index(s[i])]
                else:
                    s[i] = a1[a2.index(s[i].upper())].lower()

        return "".join(s)

    def make_cipher_alphabet(alphabet, keyword):
        newAlpha = ""
        for i in list(keyword.upper()):
            if (not i in newAlpha):
                newAlpha += i
        for i in list(alphabet):
            if (not i in newAlpha):
                newAlpha += i
        return newAlpha

    def keyword_substitution_cipher_encode(s, k, a1):
        s = list(s)
        a1 = list(a1)
        a2 = list(subCipher.make_cipher_alphabet(a1, k))

        for i in range(len(s)):
            if (s[i].upper() in a2):
                if (s[i].isupper()):
                    s[i] = a2[a1.index(s[i])]
                else:
                    s[i] = a2[a1.index(s[i].upper())].lower()

        return "".join(s)

    def keyword_substitution_cipher_decode(s, k, a1):
        s = list(s)
        a1 = list(a1)
        a2 = list(subCipher.make_cipher_alphabet(a1, k))

        for i in range(len(s)):
            if (s[i].upper() in a2):
                if (s[i].isupper()):
                    s[i] = a1[a2.index(s[i])]
                else:
                    s[i] = a1[a2.index(s[i].upper())].lower()

        return "".join(s)


class crackingTools():

    def frequent_letters(text):
        text = subCipher.prepareString(text)
        c = Counter(text)
        return c.most_common(4)

    def frequent_bigraphs(text):

        text = subCipher.prepareString(text)
        bigraphs = []
        for index in range(len(text) - 1):
            bigraphs.append(text[index:index + 2])
        c = Counter(bigraphs)
        return c.most_common(4)

    def frequent_trigraphs(text):

        text = subCipher.prepareString(text)
        trigraphs = []
        for index in range(len(text) - 1):
            trigraphs.append(text[index:index + 3])
        c = Counter(trigraphs)
        return c.most_common(4)

    def frequent_double_letters(text):
        text = subCipher.prepareString(text)
        bigraphs = []
        for index in range(len(text) - 1):
            if (text[index] == text[index + 1]):
                bigraphs.append(text[index:index + 2])
        c = Counter(bigraphs)
        return c.most_common(4)


class CLITools:

    def ceasarEncode():
        p = input("Whats the message?\n")
        s = input("Whats the shift?\n")
        ciphertext = subCipher.caesar_shift_encode(p, s, ALPHABET)
        print("\n---Encoding Caesar-------")
        print("Ciphertext = %s" % ciphertext)

    def caesarDecode():
        p = input("Do you know the shift? (y/n)")
        if (p == 'n'):
            CLITools.caesarLoop()
        else:
            c = input("What's the message?\n")
            s = input("What's the shift?\n")
            plaintext = subCipher.caesar_shift_decode(c, int(s), ALPHABET)
            print("\n---Decoding Caesar-------")
            print("Plaintext = %s" % plaintext)

    def caesarLoop():
        c = input("What's the message?\n")
        for i in range(1, 27):
            s = subCipher.caesar_shift_decode(c, i, ALPHABET)
            for j in commonWords:
                if s.find(j) >= 0:
                    print("Shift = " + str(i) + ": " + s)
                    break
            # print(str(i) + ": " + s)
        print("Tested 26 Combinations")

    def cliMain():
        w = input("Caesar or substitution? (c/s)")
        if (w == 'c'):
            CLITools.caesarMain()
        else:
            CLITools.subMain()

    def caesarMain():
        w = input("Encode or Decode? (e/d)")
        if (w == 'e'):
            CLITools.caesarEncode()
        else:
            CLITools.caesarDecode()

    def subMain():
        w = input("Encode or Decode? (e/d)")
        if (w == 'e'):
            CLITools.subEncode()
        else:
            CLITools.subDecode()

    def subEncode():
        a1 = input("Enter plaintext alphabet: (Leave blank for normal A-Z)")
        if (a1 == ""):
            a1 = ALPHABET
        a2 = input("Enter new Alphabet")
        m = input("Enter message:\n")
        ciphertext = subCipher.substitution_cipher_encode(m, a1, a2)
        print("\n---Encoding Substitution Cipher-------")
        print("Ciphertext = %s" % ciphertext)

    def subDecode():
        w = input("Do you know the substitution alphabet? (y/n)")
        if (w == "y"):
            subDecodeKnown()
        else:
            subDecoder(input("What's the message?\n"))


class subDecoder():
    cipherText = ""
    cipherTextPreserved = ""
    freqTable = [0] * 26

    alphaDict = {
        "A": "",
        "B": "",
        "C": "",
        "D": "",
        "E": "",
        "F": "",
        "G": "",
        "H": "",
        "I": "",
        "J": "",
        "K": "",
        "L": "",
        "M": "",
        "N": "",
        "O": "",
        "P": "",
        "Q": "",
        "R": "",
        "S": "",
        "T": "",
        "U": "",
        "V": "",
        "W": "",
        "X": "",
        "Y": "",
        "Z": "",
    }

    def __init__(self, code):
        self.cipherText = subCipher.prepareString(code)
        self.cipherTextPreserved = code
        self.freqA(self.cipherText)
        while (True):
            f = input("Whachu wanna do?\n")
            if (f == "a"):
                q = input("Letter in cipher? ")
                self.alphaDict[q] = input("Letter in plain? ")
                print(self.alphaDict)
            elif (f == "p"):
                a1 = ""
                for i in ALPHABET:
                    if (self.alphaDict[i] != ""):
                        a1 += self.alphaDict[i]
                    else:
                        a1 += i
                a2 = ""
                for i in ALPHABET:
                    if (self.alphaDict[i] != ""):
                        a2 += self.alphaDict[i]
                    else:
                        a2 += "_"
                print("")
                print(ALPHABET)
                print(a1)
                print("")
                print(self.cipherTextPreserved + "\n")
                print(subCipher.substitution_cipher_decode(self.cipherTextPreserved, a1, ALPHABET) + "\n")
                print(subCipher.substitution_cipher_decode(self.cipherTextPreserved, a2, ALPHABET) + "\n")
                """"print("Printing current translation")
                p = self.cipherText
                for j in list(ALPHABET):
                  if(self.alphaDict[j] != ''):
                    p = list("".join(p).replace(j, self.alphaDict[j].upper()))
                  if(self.alphaDict[j] == ''):
                    p = list("".join(p).replace(j, j.lower()))
                print("".join(p))
                """
            elif (f == "f"):
                self.freqA(self.cipherText)
            elif (f == "k"):
                self.keyWordAttack()

    def freqA(self, c):
        self.freqTable = [0] * 26
        c = list(c)
        for i in c:
            self.freqTable[ALPHABET.find(i)] += 1
        for i in range(26):
            print(ALPHABET[i] + ": " + str(self.freqTable[i]))
        c = "".join(c)
        print(crackingTools.frequent_letters(c))
        print(crackingTools.frequent_bigraphs(c))
        print(crackingTools.frequent_trigraphs(c))
        print(crackingTools.frequent_double_letters(c))

    def keyWordAttack(self):
        count = 0
        c = 0
        for i in manyWords:
            c = 0
            l = subCipher.substitution_cipher_decode(self.cipherText, ALPHABET,
                                                     subCipher.make_cipher_alphabet(ALPHABET, i))
            con = "BCDFGHJKLMNPQRSTVWXYZ"
            if (not (l[0] in con and l[1] in con and l[2] in con)):
                for m in commonWords:
                    if m in l:
                        c = c + 1
                        if (c > 2):
                            print(i + ": " + l + "\n")
                            count = count + 1
                            break
        print(str(len(manyWords)) + " words tested. " + str(count) + " hits.")

    def randKeyWord(self):
        print("nah")