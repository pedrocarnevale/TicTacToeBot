from enum import Enum
import pygame

class GameState(Enum):
    NOT_FINISHED = 0
    DEFEAT = 1
    TIE = 2
    WIN = 3

class Char(Enum):
    EMPTY = 0
    X = 1
    O = 2

class BotType(Enum):
    MINIMAX = 0
    RANDOM = 1

class Button():
    def __init__(self, text, x, y, color, textSize, width, height):
        self.__text = text
        self.__x = x
        self.__y = y
        self.__color = color
        self.__width = width
        self.__height = height
        self.__textSize = textSize
        self.__isClicked = False

    def draw(self, window):
        if self.__isClicked:
            pygame.draw.rect(window, gameConfig['clickedColor'], (self.__x, self.__y, self.__width, self.__height))
        else:
            pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__width, self.__height))
        font = pygame.font.SysFont("comicsansms", self.__textSize)
        text = font.render(self.__text, True, (255, 255, 255))
        window.blit(text, (self.__x + round(self.__width / 2) - round(text.get_width() / 2),
                        self.__y + round(self.__height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        return (self.__x <= x1 <= self.__x + self.__width) and (self.__y <= y1 <= self.__y + self.__height)

    def setIsClicked(self, isClicked):
        self.__isClicked = isClicked

    def getIsClicked(self):
        return self.__isClicked

fontsConfig = {
            'charFont': pygame.font.SysFont("comicsansms", 120),
            'bigFont': pygame.font.SysFont("comicsansms", 40),
            'smallFont': pygame.font.SysFont("comicsansms", 20),
            'mediumFont': pygame.font.SysFont("comicsansms", 30),
            'titleColor': (255, 255, 255),
            'scoreColor': (0, 255, 255),
            'xColor': (200, 0, 0),
            'oColor': (0, 200, 0),
            'lineColor': (255, 255, 255),
            'textColor': (255, 255, 255),
        }

gameConfig = {
            'width': 700,
            'height': 700,
            'boardSize': 400,
            'boardPos': (150, 200),
            'screenColor': (0, 0, 100),
            'clickedColor': (0, 0, 50),
            'titleText': fontsConfig['bigFont'].render("Tic Tac Toe", True, fontsConfig['titleColor']),
            'titlePos': (250, 0),
            'namesPos': (0, 60),
            'roundPos': (0, 650),
            'scorePos': (250, 80),
            'oText': fontsConfig['charFont'].render('O', True, fontsConfig['oColor']),
            'xText': fontsConfig['charFont'].render('X', True, fontsConfig['xColor']),
            'charOffset': (20, -20)
         }