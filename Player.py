class Player:
    def __init__(self, name, char):
        self.__score = 0
        self.__name = name
        self.__char = char

    def getScore(self):
        return self.__score

    def getName(self):
        return self.__name

    def getChar(self):
        return self.__char