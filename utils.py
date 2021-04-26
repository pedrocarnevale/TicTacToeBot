from enum import Enum
import pygame

class Char(Enum):
    EMPTY = 0
    X = 1
    O = 2

class Mode(Enum):
    SINGLEPLAYER = 0
    MULTIPLAYER = 1

class Button():
    def __init__(self, text, x, y, color, textSize, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.textSize = textSize

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsansms", self.textSize)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        return (self.x <= x1 <= self.x + self.width) and (self.y <= y1 <= self.y + self.height)

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