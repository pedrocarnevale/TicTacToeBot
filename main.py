import pygame
pygame.init()
pygame.font.init()

from utils import gameConfig
from Menu import Menu
from Environment import Environment

window = pygame.display.set_mode((gameConfig['width'], gameConfig['height']))
pygame.display.set_caption("TicTacToe")
clock = pygame.time.Clock()

players = []
menu = Menu(players, window)

while menu.isWindowRunning():
    menu.update()
    menu.draw()

players = menu.getPlayers()

environment = Environment(players, window)

while True:
    clock.tick(60)
    environment.update()
    environment.draw()