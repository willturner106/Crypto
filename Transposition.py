# Will Turner 2020

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]

manyWords = open('WordLists/morewords.txt', 'r').readlines()
manyWords = [manyWords[x][0:len(manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(manyWords) - 1)]


def decode(cipher, key):
    """
    Decode a transposition-encyphered string

    :param str cipher: The string to be decoded
    :param int key: The number of columns used to encode
    :return: The decoded string
    """
    return decryptTranspose(cipher, key)


def encode(plain, key):
    """
    Encode a string using a transposition cipher

    :param str plain: The plaintext to be encoded
    :param int key: The number of columns used to encode
    :return: The encoded string
    """
    return transpose(plain, key)


def transpose(plain, key):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plain):
            ciphertext[col] += plain[pointer]
            pointer += key
    return ''.join(ciphertext)


def decryptTranspose(cipher, key):

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

    return output

def keyWord(cipher, word):

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
                    switch(matrix[i], l, l + 1)

    # print(word)
    output = ""
    for item in matrix:
        # print(item)
        for l in item:
            output += l

    return output

def switchRow(l, a, b):
    for i in range(len(l)):
        switch(l[i], int(a), int(b))
    return l

def decodeUnkownWord(cipher, keyLength):
    key = keyLength
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
        print(cipher)

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
    for item in matrix:
        print(item)

    while (True):
        a = input()
        b = input()
        switchRow(matrix, a, b)
        numThing = [str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10),
                    str(11)]
        print(numThing)
        output = ""
        for item in matrix:
            print(item)
            for l in item:
                output += l

        print(output)

def spamCaesar(cipher):
    count = 0
    for i in manyWords:
        c = 0
        s = keyWord(cipher, i)
        for z in range(1, 27):
            l = caesar_shift_decode(s, z, ALPHABET)
            con = "BCDFGHJKLMNPQRSTVWXYZ"
            if (not (l[0] in con and l[1] in con and l[2] in con) and (
                    l[len(l) - 1] == 'X' and l[len(l) - 2] == 'X')):
                for m in commonWords:
                    if m in l:
                        c = c + 1
                        if (c > 1):
                            print(str(i) + " - " + str(z) + ": " + l + "\n")
                            count = count + 1
                            break
    print(str(len(manyWords)) + " words tested. " + str(count) + " hits.")

def spam(cipher):
    count = 0
    for i in manyWords:
        c = 0
        l = keyWord(cipher, i)
        con = "BCDFGHJKLMNPQRSTVWXYZ"
        if (not (l[0] in con and l[1] in con and l[2] in con) and (l[len(l) - 1] == 'X' and l[len(l) - 2] == 'X')):
            for m in commonWords:
                if m in l and len(i) == 5:
                    c = c + 1
                    if (c > -1):
                        print(str(i) + ": " + l + "\n")
                        count = count + 1
                        break
        if (len(i) == 5 and list(l)[0] == "A"):
            print(str(i) + ": " + l + "\n")
    print(str(len(manyWords)) + " words tested. " + str(count) + " hits.")

def decodeUnkownWordUnfilled(cipher, keyLength):
    # cipher = caesar_shift_decode(cipher, 14, ALPHABET)
    key = keyLength
    ogC = cipher
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
        print(cipher)

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
    for item in matrix:
        print(item)

    while (True):
        a = input()
        b = input()
        switchRow(matrix, a, b)
        numThing = [str(0), str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10),
                    str(11)]

        io = ""
        for l in range(len(matrix[0])):
            for i in range(len(matrix)):
                io += matrix[i][l]

        output = ""
        for item in matrix:
            for l in item:
                output += l
        output = output.replace("X", '')
        print(output)
        output = addX(io, keyLength)
        matrix = makeMatrix(output, keyLength)

        print(numThing)
        for item in matrix:
            print(item)
        print(output)

def addX(cipher, key):
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
    return cipher

def makeMatrix(cipher, key):
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
    return matrix

def switch(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def decodeUnkownColumns(cipher):
    x = 2
    while (True):
        print(x, decryptTranspose(cipher, x))
        x += 1
        t = input()

def caesar_shift_decode(p, s, a):
    result = ""
    a1 = a.upper()
    a2 = a.lower()
    for i in range(len(p)):
        char = p[i]
        if (char in a1):
            result += i2c((c2i(char, a1) - s) % len(a1), a1)
        elif (char in a2):
            result += i2c((c2i(char, a2) - s) % len(a2), a2)
        else:
            result += char
    return result

def c2i(c, alphabet):
    return alphabet.index(c)

def i2c(i, alphabet):
    return list(alphabet)[i]


cipherText = "UCIERCTTMITENOAOIOOKDIRCOGEVJRAIESONZCTTISNEAAOFBSTSAZHNNBRNMCMSOHBHFALOULZGROSEIHSSNPWXEHCYIAOEPLNLGRZSTTLYET"

# decodeUnkownWordUnfilled(cipherText, 5)
#spam(cipherText)
