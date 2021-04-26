import pygame
import sys
from utils import fontsConfig
from utils import gameConfig
from utils import Button
from utils import Mode

class GameModeMenu:
    def __init__(self, window):

        self.__running = True

        self.__clock = pygame.time.Clock()

        self.__singlePlayerButton = Button("Single Player", gameConfig['width'] * 0.29, gameConfig['height'] * 0.3,
                                         (255, 128, 0), 50, 320, 100)
        self.__multiPlayerButton = Button("Multiplayer", gameConfig['width'] * 0.3, gameConfig['height'] * 0.6,
                                          (128, 0, 128), 50, 300, 100)

        self.__mode = Mode.SINGLEPLAYER

        self.__window = window

    #returns the game mode chosen
    def update(self):

        while self.__running:
            self.__clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if self.__singlePlayerButton.click(pos):
                        self.__mode = Mode.SINGLEPLAYER
                        self.__running = False

                    if self.__multiPlayerButton.click(pos):
                        self.__mode = Mode.MULTIPLAYER
                        self.__running = False

            self.draw()

    def draw(self):

        self.__window.fill(gameConfig['screenColor'])

        #Draw title
        welcomeText = fontsConfig['bigFont'].render("Welcome to Tic Tac Toe!", True, fontsConfig['titleColor'])
        self.__window.blit(welcomeText, (gameConfig['width'] * 0.16, 0))

        #DrawButtons
        self.__singlePlayerButton.draw(self.__window)
        self.__multiPlayerButton.draw(self.__window)

        pygame.display.update()

    def getMode(self):
        return self.__mode