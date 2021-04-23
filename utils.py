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
            'titleText': fontsConfig['bigFont'].render("Tic Tac Toe", True, fontsConfig['titleColor']),
            'titlePos': (250, 0),
            'namesPos': (0, 60),
            'roundPos': (0, 650),
            'scorePos': (250, 80),
            'oText': fontsConfig['charFont'].render('O', True, fontsConfig['oColor']),
            'xText': fontsConfig['charFont'].render('X', True, fontsConfig['xColor']),
            'charOffset': (20, -20)
         }