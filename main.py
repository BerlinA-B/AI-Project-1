# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from boardGame import Board
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    board.makeBoard("C:\\Users\\isaac\\Desktop\\AI Project 1\\AI-Project-1\\Sample_Input.txt")
    print("...")
    board.printBoard()
    print(":::")
    board.moveUp()
    print("<<<")
    board.printBoard()
    print("---")
    print(board.heuristicAlgo())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
