from Crypto import *
from math import gcd

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]

manyWords = open('WordLists/morewords.txt', 'r').readlines()
manyWords = [manyWords[x][0:len(manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(manyWords) - 1)]

wordList = open('WordLists/evenmorewords.txt', 'r').readlines()
wordList = [wordList[x][0:len(wordList[x]) - 1].replace(" ", "").upper().replace(".", "").replace("-", "").replace("&","").replace("$", "").replace("/", "").replace("'", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("!", "") for x in range(len(wordList) - 1)]


class AffineCracker:

    def __init__(self, ciphertext, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.ciphertext = ciphertext
        self.alphabet = alphabet
        self.affine = Affine(cipher=ciphertext, alpha=alphabet)

    def spam(self, tolerance=3):
        mostLikely = []
        mod = len(self.alphabet)
        count = 0
        nums = AffineCracker.listAValues(mod)
        for i in nums:
            for m in range(mod):

                self.affine.a = int(i)
                self.affine.b = m
                l = self.affine.decode()

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
            if (AffineCracker.isAValue(a, m)):
                num.append(str(a))
        return num

    @staticmethod
    def isAValue(a, m):
        if (gcd(a, m) == 1):
            return True
        return False


code = "KI KIXAS.KAQGO XATYWASG MAGYSKHAM HDTYPHZTSM TG T DLUHASKIFNSZFSTU XWTX XWAV RZLIM UZSA MKRRKYLDX XWTI ZXWASXAYWIZDZFKAG TIM UZSA DKPADV XZ UTDRLIYXKZIC XWA GYWZZDMKGXSKYX QTG NDTIIKIF XZ GQKXYW XZ TIZXWAS ZIDKIA NDTXRZSUOGYWZZDZFV YTDMQADD GTKMC TWATM ZR XWTXO RTKSRTE XATYWASGWTM HAFLI SADVKIF ZI FZZFDA YDTGGSZZUO TI ZIDKIA NDTXRZSUXWAV GTQ TG UZSA LGASRSKAIMDV TIM TYYAGGKHDAC UTIV QASAYTLFWX RDTXRZZXAM HV XWA GLMMAI SA.ASGKZI XZ HDTYPHZTSMC"
a = AffineCracker(ciphertext=code, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.")
print(a.spam())
