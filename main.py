import pygame
pygame.init()
pygame.font.init()

from Player import *
from Environment import *

player = Player('Pedro', Char.X)
bot = Player('Bot', Char.O)

players = [player, bot]

environment = Environment(players)

environment.update()