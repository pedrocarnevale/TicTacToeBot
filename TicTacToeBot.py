from utils import MiniMaxState
from utils import Char
from utils import fontsConfig
from utils import GameState
from GameFunctions import checkGameState
from GameFunctions import numEmptyCells
import copy

class TicTacToeBot:
    def __init__(self, name, char):
        self.__name = name
        self.__char = char
        self.__score = 0

    def minValue(self, state, alpha, beta):

        nextStates = state.getNextStates()

        if len(nextStates) == 0:
            return state.getValue()

        state.setValue(float('inf'))

        for newState in nextStates:
            newValue = self.maxValue(newState, alpha, beta)

            if newValue < state.getValue():
                state.setValue(newValue)

            if newValue <= alpha:
                return state.getValue()

            if newValue < beta:
                beta = newValue

        return state.getValue()

    def maxValue(self, state, alpha, beta):
        nextStates = state.getNextStates()

        if len(nextStates) == 0:
            return state.getValue()

        state.setValue(float('-inf'))

        for newState in nextStates:
            newValue = self.minValue(newState, alpha, beta)

            if newValue > state.getValue():
                state.setValue(newValue)

            if newValue >= beta:
                return state.getValue()

            if newValue > alpha:
                alpha = newValue

        return state.getValue()

    def createStateTree(self, env, currState, char):
        board = currState.getBoard()

        gameState = checkGameState(board, char)

        if gameState == GameState.NOT_FINISHED:
            for line in board:
                for cell in line:
                    if cell.getChar() == Char.EMPTY:
                        move = cell.getCellNumber()

                        newBoard = copy.deepcopy(board.copy())
                        newBoard[move // 3][move % 3].setChar(char)

                        nextState = MiniMaxState(newBoard, move)

                        if char == Char.X:
                            self.createStateTree(env, nextState, Char.O)

                        elif char == Char.O:
                            self.createStateTree(env, nextState, Char.X)

                        else:
                            raise Exception("Programa melhor essa bagaça")

                        currState.addNextState(nextState)
        else:
            numEmpty = numEmptyCells(board)

            if gameState == GameState.WIN:
                currState.setValue(numEmpty)

            elif gameState == GameState.DEFEAT:
                currState.setValue(-numEmpty)

            else:
                currState.setValue(0)

    def calculateNextMove(self, environment, board):

        currState = MiniMaxState(board)

        self.createStateTree(environment, currState, self.__char)
        self.maxValue(currState, float('-inf'), float('inf'))

        nextStates = currState.getNextStates().copy()

        bestScore = float('-inf')

        nextMove = -1

        for state in nextStates:
            if state.getValue() > bestScore:
                bestScore = state.getValue()
                nextMove = state.getMove()

        if nextMove < 0:
            raise Exception("Programe melhor essa logica")

        return nextMove

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

