from utils import MiniMaxState
from utils import Char
from utils import fontsConfig
from utils import GameState
from GameFunctions import checkGameState
from GameFunctions import numEmptyCells
from GameFunctions import randomEmptyPosition
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

    def createStateTree(self, currState, char):
        board = currState.getBoard()

        gameState = checkGameState(board, self.__char)

        if gameState == GameState.NOT_FINISHED:
            for line in board:
                for cell in line:
                    if cell.getChar() == Char.EMPTY:
                        move = cell.getCellNumber()

                        newBoard = copy.deepcopy(board.copy())
                        newBoard[move // 3][move % 3].setChar(char)

                        nextState = MiniMaxState(newBoard, move)

                        if char == Char.X:
                            self.createStateTree(nextState, Char.O)

                        else:
                            self.createStateTree(nextState, Char.X)

                        currState.addNextState(nextState)

        else:
            numEmpty = numEmptyCells(board) + 1

            if gameState == GameState.WIN:
                currState.setValue(numEmpty)

            elif gameState == GameState.DEFEAT:
                currState.setValue(-numEmpty)

            else:
                currState.setValue(0)
            #for i in range(0, 3):
            #    print(board[i])

            #print(currState.getValue())
            #print("\n")

    def calculateNextMove(self, board):

        currState = MiniMaxState(board)
        nextMove = -1

        #if numEmptyCells(board) > 7:
        #    return randomEmptyPosition(board)

        self.createStateTree(currState, self.__char)
        self.maxValue(currState, float('-inf'), float('inf'))

        nextStates = currState.getNextStates().copy()

        bestScore = float('-inf')

        for state in nextStates:
            if state.getValue() > bestScore:
                bestScore = state.getValue()
                nextMove = state.getMove()

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

