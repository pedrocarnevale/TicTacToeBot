import pygame
import sys
from utils import fontsConfig
from utils import gameConfig
from utils import Button
from utils import Char
from utils import BotType
from Player import Player
from TicTacToeBot import TicTacToeBot

class Menu:
    def __init__(self, players, window, playerChar = Char.EMPTY):
        self.__buttons = [[[], [], []], [[], []]]
        self.__buttons[0][0] = Button("Person", gameConfig['width'] * 0.06, gameConfig['height'] * 0.4,
                                         (255, 128, 0), 30, gameConfig['width'] * 0.25, 60)
        self.__buttons[0][1] = Button("Random Bot", gameConfig['width'] * 0.37, gameConfig['height'] * 0.4,
                                          (128, 0, 128), 30, gameConfig['width'] * 0.25, 60)
        self.__buttons[0][2] = Button("Smart Bot", gameConfig['width'] * 0.68, gameConfig['height'] * 0.4,
                                          (128, 128, 128), 30, gameConfig['width'] * 0.25, 60)
        self.__buttons[1][0] = Button("X", gameConfig['width'] * 0.2, gameConfig['height'] * 0.6,
                                fontsConfig['xColor'], 50, 150, 100)
        self.__buttons[1][1] = Button("O", gameConfig['width'] * 0.6, gameConfig['height'] * 0.6,
                                fontsConfig['oColor'], 50, 150, 100)
        self.__finishButton = Button("Continue", gameConfig['width'] * 0.7, gameConfig['height'] * 0.9,
                                (0, 100, 0), 20, gameConfig['width'] * 0.25, 40)

        self.__nameRect = pygame.Rect(gameConfig['width'] * 0.25, gameConfig['height'] * 0.25,
                                      gameConfig['width'] * 0.5, 32)

        self.__id = 1
        self.__playerName = ""
        self.__playerChar = playerChar
        self.__players = players
        self.__running = True
        self.__window = window

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.__playerName = self.__playerName[0:-1]
                else:
                    if len(self.__playerName) <= 10 and event.key != pygame.K_RETURN:
                        self.__playerName += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if self.__id == 1:
                    for i in range(0, 2):
                        if self.__buttons[1][i].click(pos):
                            self.__buttons[1][(i + 1) % 2].setIsClicked(False)
                            self.__buttons[1][i].setIsClicked(True)

                for i in range(0, 3):
                    if self.__buttons[0][i].click(pos):
                        for button in self.__buttons[0]:
                            button.setIsClicked(False)
                        self.__buttons[0][i].setIsClicked(True)

                if self.__finishButton.click(pos):
                    self.createPlayer()

    def draw(self):
        self.__window.fill(gameConfig['screenColor'])

        #Draw title
        welcomeText = fontsConfig['bigFont'].render("Welcome to Tic Tac Toe!", True, fontsConfig['titleColor'])
        playerText = fontsConfig['mediumFont'].render("Build Player " + str(self.__id) + ":", True, fontsConfig['textColor'])
        self.__window.blit(welcomeText, (gameConfig['width'] * 0.16, 0))
        self.__window.blit(playerText, (gameConfig['width'] * 0.1, gameConfig['height'] * 0.1))

        # Draw name
        nameText = fontsConfig['mediumFont'].render("Name:", 1, fontsConfig['titleColor'])
        self.__window.blit(nameText, (gameConfig['width'] * 0.2, gameConfig['height'] * 0.17))
        texto = fontsConfig['smallFont'].render(self.__playerName, 1, (4, 15, 133))

        pygame.draw.rect(self.__window, (255, 255, 255), self.__nameRect)
        self.__window.blit(texto, (self.__nameRect.x + 5, self.__nameRect.y + 5))

        #DrawButtons
        if self.__id == 1:
            for i in range(0, 2):
                self.__buttons[1][i].draw(self.__window)

        for i in range(0, 3):
            self.__buttons[0][i].draw(self.__window)

        self.__finishButton.draw(self.__window)

        pygame.display.update()

    def createPlayer(self):
        if self.__id == 1:
            if self.__buttons[1][0].getIsClicked():
                self.__playerChar = Char.X
            elif self.__buttons[1][1].getIsClicked():
                self.__playerChar = Char.O
            else:
                return

        if self.__buttons[0][0].getIsClicked():
            self.__players.append(Player(self.__playerName, self.__playerChar))
        elif self.__buttons[0][1].getIsClicked():
            self.__players.append(TicTacToeBot(self.__playerName, self.__playerChar, BotType.RANDOM))
        elif self.__buttons[0][2].getIsClicked():
            self.__players.append(TicTacToeBot(self.__playerName, self.__playerChar, BotType.MINIMAX))
        else:
            return

        if self.__id == 1:
            self.moveToPlayer2()
        else:
            self.__running = False

    def moveToPlayer2(self):
        self.__id = 2

        for i in range(0, 3):
            self.__buttons[0][i].setIsClicked(False)

        self.__finishButton = Button("Start Game", gameConfig['width'] * 0.7, gameConfig['height'] * 0.9,
                                     (0, 100, 0), 20, gameConfig['width'] * 0.25, 40)

        self.__playerName = ""
        if self.__playerChar == Char.X:
            self.__playerChar = Char.O
        else:
            self.__playerChar = Char.X

    def isWindowRunning(self):
        return self.__running

    def getPlayers(self):
        return self.__players