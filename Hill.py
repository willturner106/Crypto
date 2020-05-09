# Will Turner 2020

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,."
mod = len(ALPHABET)


def getKeyMatrix(key):
    keyMatrix = [[0] * 2 for i in range(2)]
    key = key.split()
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = int(key[k])
            k += 1
    return keyMatrix


def inverseKey(key):
    k = getKeyMatrix(key)
    d = ((k[0][0] * k[1][1]) - (k[0][1] * k[1][0]))
    d = mod_inverse(d, mod)
    invMatrix = [[k[1][1], k[0][1] * -1], [k[1][0] * -1, k[0][0]]]

    for i in range(len(invMatrix)):
        for l in range(len(invMatrix[0])):
            invMatrix[i][l] = invMatrix[i][l] * d % mod

    return invMatrix


def mod_inverse(a, m):
    for i in range(m):
        if (i * a % m == 1):
            return i


# Following function encrypts the message
def encode(messageMatrix, key):
    keyMatrix = getKeyMatrix(key)
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

def decode(messageMatrix, key):
    return encode(messageMatrix, inverseKey(key))


def HillCipher(message, keyMatrix, alpha):
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
    cipherMatrix = encode(messageVector, keyMatrix)

    # Generate the encrypted text
    # from the encrypted vector
    CipherText = []
    for j in range(len(cipherMatrix)):
        for i in range(2):
            CipherText.append(alpha[cipherMatrix[j][i]])

            # Finally print the ciphertext
    return "".join(CipherText)


def crib(message, crib):
    for i in range(mod):
        print(round(i / mod * 100, 2), "%")
        # printProgressBar(i,mod)
        for l in range(mod):
            for m in range(mod):
                for n in range(mod):
                    keyMatrix = [[i, l], [m, n]]
                    d = HillCipher(message, keyMatrix, ALPHABET)
                    if (crib in d):
                        print(d, keyMatrix)

"""
def printProgressBar(iteration, total, length=100):
    fill = '█'
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r |%s| %s%%' % (bar, percent), end="\r")
    # Print New Line on Complete
    if iteration == total:
        print()
"""

# Driver Code
message = "THIS IS NOT A TEST"
key = "12 2 1 5"
keyMatrix = getKeyMatrix(key)
# keyMatrix = inverseKey(key)


#print(HillCipher(message, keyMatrix, ALPHABET))

# crib("KRSNXWLMTAOKRSESXU,L.CGX,,JZO,JNQUESXU,LTTJR","SEEK")
