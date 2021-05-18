import pygame
pygame.init()
pygame.font.init()

from utils import gameConfig
from utils import Mode
from utils import Char
from TicTacToeBot import TicTacToeBot
from PlayerMenu import PlayerMenu
from GameModeMenu import GameModeMenu
from Environment import Environment
from Player import Player

window = pygame.display.set_mode((gameConfig['width'], gameConfig['height']))
pygame.display.set_caption("TicTacToe")

modeMenu = GameModeMenu(window)
modeMenu.update()
mode = modeMenu.getMode()

players = []

if mode == Mode.SINGLEPLAYER:
    p1Menu = PlayerMenu(1, window)
    p1Menu.update()
    player1 = p1Menu.getPlayer()
    players.append(player1)

    p1Char = players[0].getChar()
    if p1Char == Char.X:
        p2Char = Char.O
    else:
        p2Char = Char.X

    players.append(TicTacToeBot("Bot", p2Char))

elif mode == Mode.MULTIPLAYER:
    p1Menu = PlayerMenu(1, window)
    p1Menu.update()
    player1 = p1Menu.getPlayer()
    players.append(player1)

    p1Char = players[0].getChar()
    if p1Char == Char.X:
        p2Char = Char.O
    else:
        p2Char = Char.X

    p2Menu = PlayerMenu(2, window, p2Char)
    p2Menu.update()
    player2 = p2Menu.getPlayer()
    players.append(player2)

environment = Environment(mode, players, window)

environment.update()