from utils import MiniMaxState
from utils import Char

class Bot:
    def __init__(self, board, char):
        self.__currState = MiniMaxState(board)

        self.__char = char

    def minValue(self, state, alpha, beta):

        nextStates = state.getNextStates()
        state.setValue(float('inf'))

        if len(nextStates) == 0:
            return state.getValue()

        for newState in nextStates:
            newValue = self.maxValue(newState, alpha, beta)

            if newValue < state.getValue():
                state.setValue(newValue)

            if newValue <= alpha:
                return state.getValue()

            if newValue < beta:
                beta = newValue

    def maxValue(self, state, alpha, beta):

        nextStates = state.getNextStates()
        state.setValue(float('-inf'))

        if len(nextStates) == 0:
            return state.getValue()

        for newState in nextStates:
            newValue = self.minValue(newState, alpha, beta)

            if newValue > state.getValue():
                state.setValue(newValue)

            if newValue >= beta:
                return state.getValue()

            if newValue > alpha:
                alpha = newValue

    def createStateTree(self, currState):
        board = currState.getBoard()

        for line in board:
            for cell in line:
                if cell.getChar() == Char.EMPTY:
                    move = cell.getCellNumber()

                    newBoard = board
                    newBoard[move / 3][move % 3].setChar(self.__char)

                    nextState = MiniMaxState(newBoard, move)
                    currState.addNextState(nextState)
                    self.createStateTree(nextState)

    def calculateNextMove(self):

        self.createStateTree(self.__currState)
        self.maxValue(self.__currState, float('-inf'), float('inf'))

        nextStates = self.__currState.getNextStates()

        bestScore = float('-inf')

        for state in nextStates:
            if state.getValue() > bestScore:
                bestScore = state.getValue()
                nextMove = state.getMove()

        return nextMove

