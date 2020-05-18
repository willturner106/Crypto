# Will Turner 2020

import re
import random




def encode(matrixString, keyword, plaintext):

    ran = input("Random matrix? (y/n)")
    if (ran == "y" or ran == "Y"):
        matrixString = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        random.shuffle(matrixString)
        matrixString = "".join(matrixString)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if (not len(matrixString) == 36):
        return "ERROR: Matrix not 36 characters"
    for item in list(alpha):
        if (not item in matrixString):
            return "ERROR: Matrix missing letter '" + item + "'"

    p = prepare_string(plaintext)
    matrixString = list(matrixString)
    ct = ""
    matrix = [''] * 6

    for i in range(6):
        matrix[i] = matrixString[i * 6:i * 6 + 6]

    print("ADFGVX matrix:")
    for item in matrix:
        print(item)

    for item in list(p):
        for i in range(len(matrix)):
            if item in matrix[i]:
                column = matrix[i].index(item)
                row = i
        ct += list("ADFGVX")[row]
        ct += list("ADFGVX")[column]

    # print("Transposing")
    ct = transposeEncode(ct, keyword)
    ctList = [ct[i:i + 2] for i in range(0, len(ct), 2)]

    ct = ""
    for i in ctList:
        ct += i
        ct += " "

    print("Morse:")
    print(toMorseCode(ct))
    print("UnMorse Coded:")
    print(unMorseCode(toMorseCode(ct)))
    return ct

def prepare_string(s):
    s = re.sub(r'[^\w\s]', "", s)
    s = re.sub(re.compile(r'\s+'), '', s)
    return s.upper()

def transposeEncode(string, keyword):

    ct = ""
    numColumns = len(keyword)
    matrix = [''] * numColumns
    numRows = len(string) // numColumns
    if (not len(string) % numColumns == 0):
        numRows += 1

    for i in range(len(matrix)):
        matrix[i] = [''] * numRows

    row = 0
    col = 0
    for item in list(string):
        matrix[row][col] = item
        row += 1
        if (row >= numRows):
            row = 0
            col += 1

    ak = list(keyword)
    ak.sort()

    for item in ak:
        ct += "".join(matrix[list(keyword).index(item)])

    # print("Transposition matrix:")
    # for item in matrix:
    #  print (item)

    return ct

def transposeDecode(cipher, word):
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
    print(cipher)
    for i in range(key):
        for l in range(leng // key + 1):
            if (matrix[l][i] != ":"):
                matrix[l][i] = cipherList[count]
                count += 1
    # for item in matrix:
    # print(item)

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
                    switch(matrix[i], l, l + 1)

    output = ""
    for item in matrix:
        for l in item:
            output += l

    return output.replace(":", "")

def switchRow(l, a, b):
    for i in range(len(l)):
        switch(l[i], int(a), int(b))
    return l

def switch(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def decode(matrixString, keyword, ciphertext):

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if (not len(matrixString) == 36):
        return "ERROR: Matrix not 36 characters"
    for item in list(alpha):
        if (not item in matrixString):
            return "ERROR: Matrix missing letter '" + item + "'"

    ciphertext = prepare_string(ciphertext)

    pl = transposeDecode(ciphertext, keyword)

    matrixString = list(matrixString)
    matrix = [''] * 6

    for i in range(6):
        matrix[i] = matrixString[i * 6:i * 6 + 6]

    print("ADFGVX matrix:")
    for item in matrix:
        print(item)

    ctList = [pl[i:i + 2] for i in range(0, len(pl), 2)]
    ct = ""

    for item in ctList:
        row = list("ADFGVX").index(list(item)[0])
        column = list("ADFGVX").index(list(item)[1])
        # print(item, row, column, matrix[row][column])
        ct += matrix[row][column]

    return ct

def toMorseCode(string):
    string = string.replace(" ", "")
    morse = ""
    morseDict = {
        "A": ".-",
        "D": "-..",
        "F": "..-.",
        "G": "--.",
        "V": "...-",
        "X": "-..-"

    }
    for item in list(string):
        morse += morseDict[item]
        morse += "/"
    return morse

def unMorseCode(string):
    if (list(string)[len(string) - 1] == "/"):
        string = string[:-1]
    string = string.replace(" ", "").split("/")
    morse = ""
    morseDict = {
        ".-": "A",
        "-..": "D",
        "..-.": "F",
        "--.": "G",
        "...-": "V",
        "-..-": "X"

    }
    count = 0
    for item in string:
        morse += morseDict[item]
        if (count % 2 == 1):
            morse += " "
        count += 1
    return morse
