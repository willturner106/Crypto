import re
from math import gcd
from textwrap import wrap

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]


class Affine:

    def i2c(i, ALPHABET):
        return ALPHABET[i]

    def c2i(c, ALPHABET):
        return ALPHABET.find(c)

    def prepare_string(s):
        s = re.sub(r'[^\w\s]', "", s)
        s = re.sub(re.compile(r'\s+'), '', s)
        return s.upper()

    def mod_inverse(a, m):
        for i in range(m):
            if (i * a % m == 1):
                return i
        raise ValueError("No multiplicative inverse of a within mod m")

    def affine_encode(plaintext, alphabet, a, b):
        mod = len(alphabet)
        cipher = ""
        for item in list(plaintext):
            cipher += Affine.i2c(((Affine.c2i(item, alphabet) * a) + b) % mod, alphabet)
        return cipher

    def affine_decode(ciphertext, alphabet, a, b):
        mod = len(alphabet)
        plain = ""
        a1 = Affine.mod_inverse(a, len(alphabet))
        for item in list(ciphertext):
            plain += Affine.i2c(a1 * (Affine.c2i(item, alphabet) - b) % mod, alphabet)
        return plain

    def decryptKnownMultiplier(cipher, a, alphabet):
        mod = len(alphabet)
        for i in range(mod):
            print(str(i) + ": " + Affine.affine_decode(cipher, alphabet, a, i))
        print()
        print()

    def spam(cipher, tolerance, alphabet):
        mod = len(alphabet)
        count = 0
        nums = Affine.listAValues(mod)
        for i in nums:
            for m in range(mod):
                l = Affine.affine_decode(cipher, alphabet, int(i), m)
                c = 0
                for m in commonWords:
                    if m in l:
                        c = c + 1
                        if (c > tolerance):
                            print(str(i) + ": " + l + "\n")
                            count = count + 1
                            break
        print("312 keys tested. " + str(count) + " hits.")

    def crib(cipher, crib, alphabet):
        mod = len(alphabet)
        count = 0
        nums = Affine.listAValues(mod)
        for i in nums:
            for m in range(mod):
                l = Affine.affine_decode(cipher, alphabet, int(i), m)
                if (crib in l):
                    print(str(i) + ": " + l + "\n")
                    count = count + 1
                    break
        print("312 keys tested. " + str(count) + " hits.")

    def d2i(d, alphabet):
        d = list(d)
        return (alphabet.find(d[0]) * len(alphabet)) + alphabet.find(d[1])

    def i2d(i, alpha):
        return alpha[i // len(alpha)] + alpha[i % len(alpha)]

    def affine_encode_digraphs(plain, alpha, a, b):
        mod = len(alpha) * len(alpha)
        print(mod)
        if (len(plain) % 2 == 1):
            plain += alpha[0]
        plain = wrap(plain, 2)
        print(plain)

        cipher = ""
        for item in plain:
            temp = Affine.d2i(item, alpha)
            mid = ((Affine.d2i(item, alpha) * a) + b)
            onemore = ((Affine.d2i(item, alpha) * a) + b) % mod
            tqwe = Affine.i2d(((Affine.d2i(item, alpha) * a) + b) % mod, alpha)
            print(item, temp, mid, onemore, tqwe)
            cipher += Affine.i2d(((Affine.d2i(item, alpha) * a) + b) % mod, alpha)
        return cipher

    def affine_decode_digraphs(cipher, alpha, a, b):
        mod = len(alpha) * len(alpha)
        print(mod)
        plain = ""
        cipher = wrap(cipher, 2)
        print(cipher)
        a1 = Affine.mod_inverse(a, mod)
        for item in cipher:
            plain += Affine.i2d(a1 * (Affine.d2i(item, alpha) - b) % mod, alpha)
        return plain

    # alphabet size, number of A values possible, number of B values possible, total number of transformations
    def makeTable():
        print("________________________________")
        for m in range(20, 61):
            a = len(Affine.listAValues(m))
            b = m - 1
            print(m, a, b, a * b)

    def listAValues(m):
        num = []
        for a in range(m):
            if (Affine.isAValue(a, m)):
                num.append(str(a))
        return num

    def isAValue(a, m):
        if (gcd(a, m) == 1):
            return True
        return False


text = ""
result = ""

# Affine.makeTable()
# print(Affine.numAValues(17576))
# result = Affine.affine_encode(text,ALPHA,5,10)
# result = Affine.affine_decode(text,ALPHA,5,10)
# result = Affine.spam(text, 0, ALPHA)
# result = Affine.crib(text, "", ALPHA)
# result = Affine.affine_encode_digraphs(text, ALPHA, 81,119)
# result = Affine.affine_decode_digraphs(text, ALPHA, 81, 119)

print(result)