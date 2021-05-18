from utils import Char
from utils import GameState
import random

def checkWinLines(board, char):
    for line in range(0, 3):
        char0 = board[line][0].getChar()
        char1 = board[line][1].getChar()
        char2 = board[line][2].getChar()
        empty = Char.EMPTY

        if char0 != empty and char1 != empty and char2 != empty:
            if char0 == char1 == char2:
                if char0 == char:
                    #if char == Char.O:
                        #print("O")
                    #if char == Char.X:
                        #print("X")
                    #print(f"linha {line} - vitoria\n")
                    return GameState.WIN
                else:
                    #print(f"linha {line} - derrota\n")
                    return GameState.DEFEAT

    return GameState.NOT_FINISHED

def checkWinColumns(board, char):
    for column in range(0, 3):
        char0 = board[0][column].getChar()
        char1 = board[1][column].getChar()
        char2 = board[2][column].getChar()
        empty = Char.EMPTY

        if char0 != empty and char1 != empty and char2 != empty:
            if char0 == char1 == char2:
                if char0 == char:
                    #print(f"coluna {column} - vitoria\n")
                    return GameState.WIN
                else:
                    #print(f"{char0} {char}")
                    #print(f"coluna {column} - derrota\n")
                    return GameState.DEFEAT

    return GameState.NOT_FINISHED

def checkWinDiagonal(board, char):
    char00 = board[0][0].getChar()
    char01 = board[1][1].getChar()
    char02 = board[2][2].getChar()

    char10 = board[0][2].getChar()
    char11 = board[1][1].getChar()
    char12 = board[2][0].getChar()
    empty = Char.EMPTY

    #for i in range(0, 3):
    #   print(board[i])
    #print(f"{char00} {char01} {char02}")
    if char00 != empty and char01 != empty and char02 != empty:
        if char00 == char01 == char02:
            if char00 == char:
                #print("diagonal principal - vitoria\n")
                return GameState.WIN
            else:
                #print("diagonal principal - derrota\n")
                return GameState.DEFEAT

    #print(f"{char10} {char11} {char12}\n")
    if char10 != empty and char11 != empty and char12 != empty:
        if char10 == char11 == char12:

            if char10 == char:
                #print("diagonal secundária - vitoria\n")
                return GameState.WIN
            else:
                #print(f"{char10} {char}")
                #print("diagonal secundária - derrota\n")
                return GameState.DEFEAT

    return GameState.NOT_FINISHED

def checkTie(board):
    # If there is one cell empty so the game is still not over
    for line in board:
        for cell in line:
            if cell.getChar() == Char.EMPTY:
                return GameState.NOT_FINISHED
    #print("empate\n")
    return GameState.TIE

def checkGameState(board, char):

    gameOver1 = checkWinLines(board, char)
    if gameOver1 == GameState.WIN or gameOver1 == GameState.DEFEAT:
        return gameOver1

    gameOver2 = checkWinColumns(board, char)
    if gameOver2 == GameState.WIN or gameOver2 == GameState.DEFEAT:
        return gameOver2

    gameOver3 = checkWinDiagonal(board, char)
    if gameOver3 == GameState.WIN or gameOver3 == GameState.DEFEAT:
        return gameOver3

    gameOver4 = checkTie(board)
    #print('\n')
    return gameOver4

def numEmptyCells(board):

    numEmpty = 0

    for line in board:
        for cell in line:
            if cell.getChar() == Char.EMPTY:
                numEmpty += 1

    return numEmpty

def randomEmptyPosition(board):
    possibilities = []
    for i in range(0, 9):
        if board[int(i / 3)][i % 3].getChar() == Char.EMPTY:
            possibilities.append(i)

    return possibilities[random.randint(0, len(possibilities) - 1)]