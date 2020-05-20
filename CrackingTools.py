from Crypto import *
from math import gcd
from langdetect import detect

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]

manyWords = open('WordLists/morewords.txt', 'r').readlines()
manyWords = [manyWords[x][0:len(manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(manyWords) - 1)]

wordList = open('WordLists/evenmorewords.txt', 'r').readlines()
wordList = [wordList[x][0:len(wordList[x]) - 1].replace(" ", "").upper().replace(".", "").replace("-", "").replace("&","").replace("$", "").replace("/", "").replace("'", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("!", "") for x in range(len(wordList) - 1)]


class AffineDecoder(Affine):

    def __init__(self, ciphertext, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        Affine.__init__(self, cipher=ciphertext, alpha=alpha)

    def spam(self, tolerance=3):
        mostLikely = []
        mod = len(self.alpha)
        count = 0
        nums = AffineDecoder.listAValues(mod)
        for i in nums:
            for m in range(mod):

                self.a = int(i)
                self.b = m
                l = self.decode()

                c = 0
                for m in commonWords:
                    if m in l:
                        c = c + 1
                        if c > tolerance:
                            mostLikely.append(l)
                            count = count + 1
                            break

        return mostLikely

    @staticmethod
    def listAValues(m):
        num = []
        for a in range(m):
            if (AffineDecoder.isAValue(a, m)):
                num.append(str(a))
        return num

    @staticmethod
    def isAValue(a, m):
        if (gcd(a, m) == 1):
            return True
        return False


class HillDecoder(Hill):
    
    def __init__(self, ciphertext, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        Hill.__init__(self, cipher=ciphertext, alpha=alpha)
    
    def spam(self, tolerance=3):
        p = []
        mod = len(self.alpha)
        for i in range(mod):
            print(round(i / mod * 100, 2), "%")
            for l in range(mod):
                for m in range(mod):
                    for n in range(mod):
                        try:
                            self.invMatrix = self.inverseKey(str(i) + " " + str(l) + " " + str(m) + " " + str(n))
                            d = self.decode()
                            if(Helpers.isEnglish(d, tolerance)):
                                p.append(d)
                            if("DEAR" in d):
                                p.append(d)
                        except:
                            pass
        return p


class Helpers:
    
    @staticmethod
    def isEnglish(string, tolerance):
        c = 0
        for m in commonWords:
            if m in string:
                c = c + 1
                if c > tolerance:
                    return True
        return False

code = "RVRWTKVHIATOYYBPMSAWRHOWGHOGIALCVRTONAEEHQTUHAUKQPDQXU"
h = HillDecoder(ciphertext=code, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(h.spam())
