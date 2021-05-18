from utils import Char
from utils import fontsConfig
from utils import GameState
from GameFunctions import getNextMoves
from GameFunctions import checkGameState
from GameFunctions import numEmptyCells
from GameFunctions import getNewBoard
import random

class TicTacToeBot:
    def __init__(self, name, char):
        self.__name = name
        self.__char = char
        self.__score = 0

    def minValue(self, board, alpha, beta, char):
        gameState = checkGameState(board, self.__char)
        if gameState != GameState.NOT_FINISHED:
            numEmpty = numEmptyCells(board)
            numEmptyScore = numEmpty + 1

            if gameState == GameState.WIN:
                return numEmptyScore, None

            elif gameState == GameState.DEFEAT:
                return -numEmptyScore, None

            else:
                return 0, None

        value = float('inf')
        bestMove = None
        nextMoves = getNextMoves(board)

        for move in nextMoves:
            if char == Char.X:
                newValue = self.maxValue(getNewBoard(board, move, char), alpha, beta, Char.O)[0]
            else:
                newValue = self.maxValue(getNewBoard(board, move, char), alpha, beta, Char.X)[0]

            if newValue < value:
                bestMove = move
                value = newValue

            if newValue < beta:
                beta = newValue

            if beta <= alpha:
                break
        #print(bestMove)
        return value, bestMove

    def maxValue(self, board, alpha, beta, char):
        gameState = checkGameState(board, self.__char)
        if gameState != GameState.NOT_FINISHED:
            numEmpty = numEmptyCells(board)
            numEmptyScore = numEmpty + 1

            if gameState == GameState.WIN:
                return numEmptyScore, None

            elif gameState == GameState.DEFEAT:
                return -numEmptyScore, None

            else:
                return 0, None

        value = float('-inf')
        bestMove = None
        nextMoves = getNextMoves(board)

        for move in nextMoves:
            if char == Char.X:
                newValue = self.minValue(getNewBoard(board, move, char), alpha, beta, Char.O)[0]
            else:
                newValue = self.minValue(getNewBoard(board, move, char), alpha, beta, Char.X)[0]

            if newValue > value:
                bestMove = move
                value = newValue

            if newValue > alpha:
                alpha = newValue

            if alpha >= beta:
                break
        #print(bestMove)
        return value, bestMove

    def calculateNextMove(self, board):
        gameState = checkGameState(board, self.__char)
        if gameState != GameState.NOT_FINISHED:
            return None

        numEmpty = numEmptyCells(board)
        if numEmpty == 9:
            return random.randint(0, 8)

        bestMove = self.maxValue(board, float('-inf'), float('inf'), self.__char)[1]
        return bestMove

    def getScore(self):
        return self.__score

    def getName(self):
        return self.__name

    def getChar(self):
        return self.__char

    def getText(self):
        string = str(self.__name) + ": " + str(self.__score)
        return fontsConfig['mediumFont'].render(string, True, fontsConfig['titleColor'])

    def setScore(self, score):
        self.__score = score