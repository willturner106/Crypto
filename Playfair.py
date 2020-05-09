# Will Turner 2020

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

commonWords = open('WordLists/common.txt', 'r').readlines()
commonWords = [commonWords[x][0:len(commonWords[x]) - 1].replace(" ", "").upper() for x in range(len(commonWords) - 1)]

manyWords = open('WordLists/MoreWords.txt', 'r').readlines()
manyWords = [manyWords[x][0:len(manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(manyWords) - 1)]


def decode(string, word):
    grid = makeGrid(word)
    # for item in grid:
    #  print(item)
    return decodeWithGrid(string, grid)

def decodeWithGrid(string, grid):
    plain = ""

    cipher = string.split(" ")

    for item in cipher:
        first = getLocation(list(item)[0], grid)
        second = getLocation(list(item)[1], grid)

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

def makeGrid(word):
    word = word.replace("J", "")
    grid = [''] * 5
    for x in range(len(grid)):
        grid[x] = [''] * 5

    string = ""

    for item in word:
        if not item in string:
            string += item
    for item in ALPHABET:
        if not item in string:
            string += item

    string = list(string)
    count = 0
    for i in range(len(grid)):
        for l in range(len(grid[0])):
            grid[i][l] = string[count]
            count += 1
    return grid

def getLocation(letter, grid):
    for i in range(len(grid)):
        for l in range(len(grid[i])):
            if (grid[i][l] == letter):
                return (i, l)

def spam(string, tolerance):
    count = 0

    for item in manyWords:
        l = decode(string, item)
        c = 0
        for m in commonWords:
            if m in l:
                c = c + 1
                if (c > tolerance):
                    print(item + ": " + l + "\n")
                    count = count + 1
                    break
    print(str(len(manyWords)) + " words tested. " + str(count) + " hits.")

def crackWithCrib(string, crib):
    count = 0

    for item in manyWords:
        l = decode(string, item)
        c = 0
        for m in commonWords:
            if crib in l:
                print(item + ": " + l + "\n")
                count = count + 1
                break
    print(str(len(manyWords)) + " words tested. " + str(count) + " hits.")

def cribWithMoreWords(string, crib):
    wordList = open('EvenMoreWords.txt', 'r').readlines()
    wordList = [
        wordList[x][0:len(wordList[x]) - 1].replace(" ", "").upper().replace(".", "").replace("-", "").replace("&",
                                                                                                               "").replace(
            "$", "").replace("/", "").replace("'", "").replace("0", "").replace("1", "").replace("2", "").replace(
            "3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace(
            "9", "").replace("!", "") for x in range(len(wordList) - 1)]

    count = 0

    for item in wordList:
        try:
            l = decode(string, item)
        except:
            print("Error with word:", item)
        c = 0
        for m in commonWords:
            if crib in l:
                print(item + ": " + l + "\n")
                count = count + 1
                break
    print(str(len(wordList)) + " words tested. " + str(count) + " hits.")


crib = "DONOTDWE"
c = "IW OQ RE XD KZ GK QA KC AR QY IW OQ RE TD PN SD AK FB XP WP FD QO DF QA TR EK AK BQ HO IW QA KC AT FQ CQ PQ QN CQ ET"

cipher = ""
keyword = ""

# decode(cipher, keyword)
# decodeWithGrid(cipher)
# crackWithCrib(c, crib)
# cribWithMoreWords(c,crib)
