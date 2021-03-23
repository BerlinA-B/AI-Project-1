import pandas as pd
import numpy as np

class Board:

    def __init__(self):
        self.orgTable = []
        self.curTable = []
        self.goalTable = []

    def makeBoard(self,filename):
        continue

    def printBoard(self,letter):
        if letter == "o" or letter == "O":
            board=self.orgTable
        elif letter == '"c" or letter == "C":
            board=self.curTable
        else:
            board = self.goalTable

        for ele in board:
            print(*ele)
    

    def makeMove(self):
        continue

    def heuisticAlgo(self):
        continue

    
