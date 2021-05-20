from utils import gameConfig
from utils import fontsConfig
from utils import Char
from utils import GameState
from Cell import Cell
from GameFunctions import checkGameState
from TicTacToeBot import TicTacToeBot
import sys

import pygame

class Environment:
    def __init__(self, players, window):
        self.__window = window
        self.__round = 0
        self.__players = players
        self.__currPlayer = 0
        self.__board = [[], [], []]

        for i in range(0, 9):
            line = int(i / 3)
            newCell = Cell(i)
            self.__board[line].append(newCell)

    def update(self):
        isBotTurn = type(self.__players[self.__currPlayer]) is TicTacToeBot
        if type(self.__players[self.__currPlayer]) is TicTacToeBot:
            move = self.__players[self.__currPlayer].calculateNextMove(self.__board)
            botChar = self.__players[self.__currPlayer].getChar()

            self.roundUpdate(move, botChar)
            pygame.time.delay(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not isBotTurn:
                position = pygame.mouse.get_pos()
                for line in self.__board:
                    for cell in line:
                        if cell.contains(position) and cell.getChar() == Char.EMPTY:
                            playerChar = self.__players[self.__currPlayer].getChar()
                            self.roundUpdate(cell.getCellNumber(), playerChar)

    def roundUpdate(self, move, char):
        self.__board[move // 3][move % 3].setChar(char)

        gameState = checkGameState(self.__board, char)
        if gameState == GameState.NOT_FINISHED:
            self.__currPlayer = (self.__currPlayer + 1) % 2

        else:
            self.restart()
            self.endGame(gameState)
            if type(self.__players[0]) is not TicTacToeBot or type(self.__players[0]) is not TicTacToeBot:
                pygame.time.delay(2000)

    def draw(self):
        self.__window.fill(gameConfig['screenColor'])

        #Draw title
        self.__window.blit(gameConfig['titleText'], gameConfig['titlePos'])

        #Draw names and scores
        self.__window.blit(self.__players[0].getText(), gameConfig['namesPos'])
        self.__window.blit(self.__players[1].getText(), (gameConfig['namesPos'][0], gameConfig['namesPos'][1] + 40))

        #Draw board
        bSize = gameConfig['boardSize']
        boardPos = gameConfig['boardPos']

        x = boardPos[0]
        y = boardPos[1]

        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + bSize / 3, y + 0), (x + bSize / 3, y + bSize))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 2 * bSize / 3, y + 0), (x + 2 * bSize / 3, y + bSize))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 0, y + bSize / 3), (x + bSize, y + bSize / 3))
        pygame.draw.line(self.__window, fontsConfig['lineColor'], (x + 0, y + 2 * bSize / 3), (x + bSize,y + 2 * bSize / 3))

        #Draw characters
        for line in self.__board:
            for cell in line:
                offSet = gameConfig['charOffset']
                x = offSet[0]
                y = offSet[1]

                if cell.getChar() == Char.X:
                    self.__window.blit(gameConfig['xText'], (x + cell.getArea().left, y + cell.getArea().top))
                elif cell.getChar() == Char.O:
                    self.__window.blit(gameConfig['oText'], (x + cell.getArea().left, y + cell.getArea().top))

        # Round
        roundText = fontsConfig['mediumFont'].render("Round: " + str(self.__round), True, fontsConfig['titleColor'])
        self.__window.blit(roundText, gameConfig['roundPos'])

        pygame.display.update()

    def endGame(self, gameState):
        if gameState != GameState.TIE:
            currPlayerId = self.__currPlayer
            currPlayerName = self.__players[currPlayerId].getName()
            currPlayerScore = self.__players[currPlayerId].getScore()

            scoreText = fontsConfig['bigFont'].render(currPlayerName + " scores!!", True, fontsConfig['scoreColor'])
            self.__window.blit(scoreText, gameConfig['scorePos'])

            self.__players[currPlayerId].setScore(currPlayerScore + 1)

        else:
            scoreText = fontsConfig['bigFont'].render("Tie!!", True, fontsConfig['scoreColor'])
            self.__window.blit(scoreText, (gameConfig['scorePos'][0] + 50, gameConfig['scorePos'][1]))
        pygame.display.update()

    def restart(self):
        self.draw()

        self.__round += 1

        for line in self.__board:
            for cell in line:
                cell.restart()