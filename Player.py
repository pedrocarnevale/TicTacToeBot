from utils import fontsConfig
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

    def getText(self):
        string = str(self.__name) + ": " + str(self.__score)
        return fontsConfig['mediumFont'].render(string, True, fontsConfig['titleColor'])

    def setScore(self, score):
        self.__score = score