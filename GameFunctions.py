from utils import *

def checkWinLines(environment, board):
    for line in range(0, 3):
        char0 = board[line][0].getChar()
        char1 = board[line][1].getChar()
        char2 = board[line][2].getChar()
        empty = Char.EMPTY

        if char0 != empty and char1 != empty and char2 != empty:
            if char0 == char1 == char2:
                environment.restart()

                area1 = board[line][0].getArea()
                area2 = board[line][2].getArea()
                environment.endGame(area1, area2)
                return True

    return False


def checkWinColumns(environment, board):
    for column in range(0, 3):
        char0 = board[0][column].getChar()
        char1 = board[1][column].getChar()
        char2 = board[2][column].getChar()
        empty = Char.EMPTY

        if char0 != empty and char1 != empty and char2 != empty:
            if char0 == char1 == char2:
                environment.restart()

                area1 = board[0][column].getArea()
                area2 = board[2][column].getArea()
                environment.endGame(area1, area2)
                return True

    return False


def checkWinDiagonal(environment, board):
    char00 = board[0][0].getChar()
    char01 = board[1][1].getChar()
    char02 = board[2][2].getChar()

    char10 = board[0][2].getChar()
    char11 = board[1][1].getChar()
    char12 = board[2][0].getChar()
    empty = Char.EMPTY

    if char00 != empty and char01 != empty and char02 != empty:
        if char00 == char01 == char02:
            environment.restart()

            area1 = board[0][0].getArea()
            area2 = board[2][2].getArea()
            environment.endGame(area1, area2)
            return True

    elif char10 != empty and char11 != empty and char12 != empty:
        if char10 == char11 == char12:
            environment.restart()

            area1 = board[0][2].getArea()
            area2 = board[2][0].getArea()
            environment.endGame(area1, area2)
            return True

    return False


def checkGameOverNoWinner(environment, board):
    # If there is one cell empty so the game is still not over
    for line in board:
        for cell in line:
            if cell.getChar() == Char.EMPTY:
                return False

    # If there is no empty space, the game restarts with no winner
    environment.restart()
    return True