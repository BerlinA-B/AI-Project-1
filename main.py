# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from AStar import AStar
import sys
# Press the green button in the gutter to run the script.
def main(args):
    search = AStar(sys.argv[1])
    search.aStar()

sys.exit(main(sys.argv))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
