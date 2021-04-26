import pygame
import sys
from utils import fontsConfig
from utils import gameConfig
from utils import Button
from utils import Char
from Player import Player

class PlayerMenu:
    def __init__(self, playerID, window, playerChar = Char.EMPTY):
        self.__running = True

        self.__clock = pygame.time.Clock()

        if playerID == 1:
            self.__xButton = Button("X", gameConfig['width'] * 0.2, gameConfig['height'] * 0.7,
                                    fontsConfig['xColor'], 50, 150, 100)
            self.__oButton = Button("O", gameConfig['width'] * 0.6, gameConfig['height'] * 0.7,
                                    fontsConfig['oColor'], 50, 150, 100)

        elif playerID == 2:
            self.__beginButton = Button("Begin Game", gameConfig['width'] * 0.3, gameConfig['height'] * 0.7,
                                        (64, 128, 64), 50, 300, 100)

        self.nameRect = pygame.Rect(270, 250, 300, 32)
        self.__playerName = ""
        self.__playerID = playerID
        self.__playerChar = playerChar
        self.__window = window

    #returns the game mode chosen
    def update(self):

        while self.__running:
            self.__clock.tick(60)

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

                    if self.__playerID == 1:
                        if self.__xButton.click(pos):
                            self.__playerChar = Char.X
                            self.__running = False

                        if self.__oButton.click(pos):
                            self.__playerChar = Char.O
                            self.__running = False

                    elif self.__playerID == 2:
                        if self.__beginButton.click(pos):
                            self.__running = False


            self.draw()

    def draw(self):

        self.__window.fill(gameConfig['screenColor'])

        #Draw title
        welcomeText = fontsConfig['bigFont'].render("Player " + str(self.__playerID) + ":", True, fontsConfig['titleColor'])
        self.__window.blit(welcomeText, (gameConfig['width'] * 0.4, 0))

        #Draw name
        nameText = fontsConfig['mediumFont'].render("Name:", 1, fontsConfig['titleColor'])
        self.__window.blit(nameText, (175, 240))
        texto = fontsConfig['smallFont'].render(self.__playerName, 1, (4, 15, 133))

        pygame.draw.rect(self.__window, (255, 255, 255), self.nameRect)
        self.__window.blit(texto, (self.nameRect.x + 5, self.nameRect.y + 5))

        #Draw buttons
        if self.__playerID == 1:
            self.__xButton.draw(self.__window)
            self.__oButton.draw(self.__window)

        elif self.__playerID == 2:
            self.__beginButton.draw(self.__window)

        pygame.display.update()

    def getPlayer(self):
        return Player(self.__playerName, self.__playerChar)