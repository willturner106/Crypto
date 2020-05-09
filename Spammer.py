# Will Turner 2020


class Spammer:

    def __init__(self):
        self.commonWords = open('WordLists/common.txt', 'r').readlines()
        self.commonWords = [self.commonWords[x][0:len(self.commonWords[x]) - 1].replace(" ", "").upper() for x in
                       range(len(self.commonWords) - 1)]

        self.manyWords = open('WordLists/MoreWords.txt', 'r').readlines()
        self.manyWords = [self.manyWords[x][0:len(self.manyWords[x]) - 1].replace(" ", "").upper() for x in range(len(self.manyWords) - 1)]

        self.wordList = open('EvenMoreWords.txt', 'r').readlines()
        self.wordList = [self.wordList[x][0:len(self.wordList[x]) - 1].replace(" ", "").upper().replace(".", "").replace("-", "").replace("&","").replace("$", "").replace("/", "").replace("'", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("!", "") for x in range(len(self.wordList) - 1)]

    def getCommonWords(self):
        return self.commonWords

    def getManyWords(self):
        return self.manyWords

    def getMoreWords(self):
        return self.wordList
