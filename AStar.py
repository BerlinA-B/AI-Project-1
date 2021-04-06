from boardGame import Board
import copy


class AStar:
    def __init__(self, file):
        self.board = Board()
        self.board.makeBoard(file)
        self.totalTree = []
        self.front = [(copy.deepcopy(self.board), 0, [], [self.board.heuristicAlgo()])]

    ''' Runs A Star Search'''

    def aStar(self):
        while True:
            state = self.front.pop(0)
            curBoard = state[0]
            g = state[1]
            temphist = state[2]
            tempFs = state[3]
            legalMoves = []

            # curBoard.printCurBoard()
            # print()
            # print(*temphist)
            # print(curBoard.heuristicAlgo())
            # print(*tempFs)
            # print("-----")

            if state[0].atGoal():
                self.writeOut(curBoard, temphist, tempFs)
                return
            if curBoard.moveUp():
                hist = copy.deepcopy(temphist)
                hist.append(3)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveDown()
            if curBoard.moveUpRight():
                hist = copy.deepcopy(temphist)
                hist.append(4)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveDownLeft()
            if curBoard.moveRight():
                hist = copy.deepcopy(temphist)
                hist.append(5)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveLeft()
            if curBoard.moveRightDown():
                hist = copy.deepcopy(temphist)
                hist.append(6)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveLeftUp()
            if curBoard.moveDown():
                hist = copy.deepcopy(temphist)
                hist.append(7)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveUp()
            if curBoard.moveDownLeft():
                hist = copy.deepcopy(temphist)
                hist.append(8)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveUpRight()
            if curBoard.moveLeft():
                hist = copy.deepcopy(temphist)
                hist.append(1)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveRight()
            if curBoard.moveLeftUp():
                hist = copy.deepcopy(temphist)
                hist.append(2)
                legalMoves.append((copy.deepcopy(curBoard), g + 1, hist, copy.deepcopy(tempFs)))
                curBoard.moveRightDown()

            for move in legalMoves:
                for hisMove in self.totalTree:
                    if move[0].equals(hisMove):
                        continue
                moveF = move[0].heuristicAlgo() + move[1]
                move[3].append(moveF)
                added = False
                for i in range(len(self.front)):
                    frontF = self.front[i][0].heuristicAlgo() + self.front[i][1]
                    if moveF < frontF:
                        self.front.insert(i, move)
                        self.totalTree.append(move[0])
                        added = True
                        break
                if not added:
                    self.front.append(move)
                    self.totalTree.append(move[0])

    '''Writes output to file out.txt'''

    def writeOut(self, board, hist, fs):
        file = open("out.txt", "w")
        startTable = board.startTable
        goalTable = board.goalTable

        for line in startTable:
            file.write(' '.join(line))
            file.write("\n")
        file.write("\n")
        for line in goalTable:
            file.write(' '.join(line))
            file.write("\n")
        file.write("\n")
        file.write(str(len(hist)) + "\n")
        file.write(str(len(self.totalTree)) + "\n")
        file.write(' '.join(str(item) for item in hist) + "\n")
        file.write(' '.join(str(item) for item in fs) + "\n")
