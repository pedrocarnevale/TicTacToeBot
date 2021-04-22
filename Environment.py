from utils import *
from Cell import *
from Player import *
import sys

import pygame

class Environment:
    def __init__(self, players):
        self.__window = pygame.display.set_mode((gameConfig['width'], gameConfig['height']))
        pygame.display.set_caption("TicTacToe")

        self.__clock = pygame.time.Clock()

        self.__running = True
        
        if len(players) == 1:
            self.__mode = Mode.SINGLEPLAYER
        elif len(players) == 2:
            self.__mode = Mode.MULTIPLAYER
        else:
            raise Exception("Number of players error")

        self.__players = players
        self.__currPlayer = 0

        self.__board = [[], [], []]

        for i in range(0, 9):
            line = int(i / 3)
            newCell = Cell(i)
            self.__board[line].append(newCell)

    def update(self):
        while(self.__running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()

                    for line in self.__board:
                        for cell in line:
                            if cell.contains(position):
                                offSet = gameConfig['charOffset']
                                x = offSet[0]
                                y = offSet[1]

                                if self.__players[self.__currPlayer].getChar() == Char.X:
                                    cell.setChar(Char.X)
                                else:
                                    cell.setChar(Char.O)

                                self.__currPlayer = (self.__currPlayer + 1) % 2


            self.draw()

    def draw(self):
        self.__window.fill(gameConfig['screenColor'])

        bSize = gameConfig['boardSize']
        boardPos = gameConfig['boardPos']

        x = boardPos[0]
        y = boardPos[1]

        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + bSize / 3, y + 0), (x + bSize / 3, y + bSize))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 2 * bSize / 3, y + 0), (x + 2 * bSize / 3, y + bSize))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 0, y + bSize / 3), (x + bSize, y + bSize / 3))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 0, y + 2 * bSize / 3), (x + bSize,y + 2 * bSize / 3))

        for line in self.__board:
            for cell in line:
                offSet = gameConfig['charOffset']
                x = offSet[0]
                y = offSet[1]

                if cell.getChar() == Char.X:
                    self.__window.blit(gameConfig['xText'], (x + cell.getArea().left, y + cell.getArea().top))
                elif cell.getChar() == Char.O:
                    self.__window.blit(gameConfig['oText'], (x + cell.getArea().left, y + cell.getArea().top))

        pygame.display.update()



