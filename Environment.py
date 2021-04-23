from Cell import *
from GameFunctions import *
import sys

import pygame

class Environment:

    def __init__(self, players):

        self.__window = pygame.display.set_mode((gameConfig['width'], gameConfig['height']))
        pygame.display.set_caption("TicTacToe")

        self.__clock = pygame.time.Clock()

        self.__running = True

        self.__round = 0
        
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

        while self.__running:
            self.__clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()

                    for line in self.__board:

                        for cell in line:

                            if cell.contains(position) and cell.getChar() == Char.EMPTY:

                                offSet = gameConfig['charOffset']
                                x = offSet[0]
                                y = offSet[1]

                                if self.__players[self.__currPlayer].getChar() == Char.X:
                                    cell.setChar(Char.X)
                                else:
                                    cell.setChar(Char.O)

                                #If the game is not over, change the player
                                if self.checkGameOver() == False:
                                    self.__currPlayer = (self.__currPlayer + 1) % 2
                                else:
                                    pygame.time.delay(2000)
            self.draw()

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

    def checkGameOver(self):

        gameOver1 = checkWinLines(self, self.__board)
        gameOver2 = checkWinColumns(self, self.__board)
        gameOver3 = checkWinDiagonal(self, self.__board)
        gameOver4 = checkGameOverNoWinner(self, self.__board)

        return gameOver1 or gameOver2 or gameOver3 or gameOver4

    def endGame(self, area1, area2):

        currPlayerId = self.__currPlayer
        currPlayerName = self.__players[currPlayerId].getName()
        currPlayerScore = self.__players[currPlayerId].getScore()

        scoreText = fontsConfig['bigFont'].render(currPlayerName + " scores!!", True, fontsConfig['scoreColor'])
        self.__window.blit(scoreText, gameConfig['scorePos'])

        self.__players[currPlayerId].setScore(currPlayerScore + 1)

        # Draw win line
        bSize = gameConfig['boardSize']

        initialPos = (area1.left + bSize / 6, area1.top + bSize / 6)
        finalPos = (area2.left + bSize / 6, area2.top + bSize / 6)

        pygame.draw.line(self.__window, (255, 255, 255), initialPos, finalPos, 5)
        pygame.display.update()

    def restart(self):
        self.draw()

        self.__round += 1

        for line in self.__board:
            for cell in line:
                cell.restart()