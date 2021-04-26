from utils import gameConfig
from utils import Char
import pygame


class Cell:
    def __init__(self, cellNumber):
        self.__char = Char.EMPTY
        self.__cellNumber = cellNumber

        bSize = gameConfig['boardSize']
        boardPos = gameConfig['boardPos']

        x = boardPos[0]
        y = boardPos[1]

        self.__area = pygame.Rect(x + (cellNumber % 3) * bSize / 3, y + (int(cellNumber / 3)) * bSize / 3,
                                  bSize / 3, bSize / 3)

    def restart(self):
        self.__char = Char.EMPTY

    def contains(self, point):
        return self.__area.collidepoint(point)

    def getArea(self):
        return self.__area

    def getCellNumber(self):
        return self.__cellNumber

    def getChar(self):
        return self.__char

    def setChar(self, char):
        self.__char = char