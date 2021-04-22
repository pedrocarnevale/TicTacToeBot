from enum import Enum
import pygame

class Char(Enum):
    EMPTY = 0
    X = 1
    O = 2

class Mode(Enum):
    SINGLEPLAYER = 0
    MULTIPLAYER = 1

fontsConfig = {
            'charFont': pygame.font.SysFont("comicsansms", 100),
            'bigFont': pygame.font.SysFont("comicsansms", 40),
            'smallFont': pygame.font.SysFont("comicsansms", 20),
            'mediumFont': pygame.font.SysFont("comicsansms", 30),
            'xColor': (255, 0, 0),
            'oColor': (0, 255, 0),
            'lineColor': (255, 255, 255),
            'textColor': (255, 255, 255),
        }

gameConfig = {
            'width': 500,
            'height': 500,
            'boardSize': 350,
            'boardPos': (75, 75),
            'screenColor': (0, 0, 0),
            'xText': fontsConfig['charFont'].render('X', True, fontsConfig['xColor']),
            'oText': fontsConfig['charFont'].render('O', True, fontsConfig['oColor']),
            'charOffset': (20, -20)
         }