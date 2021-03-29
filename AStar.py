from boardGame import Board
import copy

class AStar:
    def __init__(self, file):
        self.board = Board()
        self.board.makeBoard(file)
        self.front = [(copy.deepcopy(self.board), 0)]

    def aStar(self):
        while True:
            state = self.front.pop(0)
            curBoard = state[0]
            g = state[1]
            legalMoves = []

            curBoard.printBoard()
            print("-------------")

            if state[0].atGoal():
                return
            if curBoard.moveUp():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveDown()
            if curBoard.moveUpRight():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveDownLeft()
            if curBoard.moveRight():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveLeft()
            if curBoard.moveRightDown():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveLeftUp()
            if curBoard.moveDown():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveUp()
            if curBoard.moveDownLeft():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveUpRight()
            if curBoard.moveLeft():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveRight()
            if curBoard.moveLeftUp():
                legalMoves.append((copy.deepcopy(curBoard), g+1))
                curBoard.moveRightDown()

            for move in legalMoves:
                moveF = move[0].heuristicAlgo() + move[1]
                added = False
                for i in range(len(self.front)):
                    frontF = self.front[i][0].heuristicAlgo() + self.front[i][1]
                    if moveF < frontF:
                        self.front.insert(i, move)
                        added = True
                        break
                if not added:
                    self.front.append(move)
