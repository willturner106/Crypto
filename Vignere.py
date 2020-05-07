ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Vigenere:

    def encrypt(string, keyword):

        cipher = ""
        k = list(keyword)
        count = 0

        for item in list(string):
            cipher += Vigenere.vig(k[count], item)
            count += 1
            if (count >= len(keyword)):
                count = 0

        return cipher

    def vig(k, i):
        shift = ALPHABET.find(k)
        return ALPHABET[(ALPHABET.find(i) + shift) % 26]

    def unVig(k, i):
        shift = ALPHABET.find(k)
        return ALPHABET[(ALPHABET.find(i) - shift) % 26]

    def decrypt(string, keyword):
        cipher = ""
        k = list(keyword)
        count = 0

        for item in list(string):
            cipher += Vigenere.unVig(k[count], item)
            count += 1
            if (count >= len(keyword)):
                count = 0

        return cipher

    def findKeyword(cipher, plain):

        keyword = ""
        for i in range(len(cipher)):
            keyword += Vigenere.findShift(cipher[i], plain[i])
        return keyword

    def findShift(c, p):
        return ALPHABET[(ALPHABET.find(c) - ALPHABET.find(p)) % 26]


class IOC:

    def make_cosets(text, n):
        temp = 0
        c = [""] * n

        for item in list(text):
            c[temp] = c[temp] + item
            temp += 1
            if (temp >= n):
                temp = 0

        return c

    def index_of_coincidence(cipher, alpha):
        a = [0] * len(alpha)
        for item in list(cipher):
            a[alpha.find(item)] += 1
        total = 0
        for item in a:
            total += (item / len(cipher)) * ((item - 1) / (len(cipher) - 1))
        return total

    def testKeyLength(cipher, k):
        t = 0
        l = IOC.make_cosets(cipher, k)
        for item in l:
            t += IOC.index_of_coincidence(item, ALPHABET)
        return t / k


#cipher = "EVKEF XYELZ XTZUK MGKLE WUIPR EMNWN VIGKL CWHKY KPEPW LJSGE EMWXK LHDES TYRPXSYRAY UKHCH AFXAI PVPSO IIXAR LUYYJ YFFJM GHVCG VERTY UJHIH VALXH GZEBW UCIXEGRQJK IWKLE DITEM ZSNGZ KLXKV ESMLV XRRDA NJFXE IFSWK SKJMN LBIIX USCMG VRMJSNDSFR XFJTZ YJIWF GUEYE XLYES WPVVU VINVY TVRGX EVNYI XEGRQ JKIWU SCMGV RMFYTDCEMG XXHWJ IIVZW EDITE MZSNG ZKLXK VESML VXYES FYMIK SIEFX VGKPT TWXVZ XEXHGOXLFR RYHYF TEVMN UFLHB EKSGG VJKFQ TZYEW TYEVW NIMXU"
#cipher = cipher.replace(" ", "")
#plain = ""
#keyword = "TREASURE"
#keyLength = 0

# -----Index of Coincidence-----#
# IOC.index_of_coincidence(cipher,ALPHABET)
# IOC.make_cosets(cipher, keyLength)
# IOC.testKeyLength(cipher, keyLength)

# -----Vigenere-----#
# Vigenere.encrypt(plain, keyword)
#print(Vigenere.decrypt(cipher, keyword))
# Vigenere.findKeyword(cipher,plain)