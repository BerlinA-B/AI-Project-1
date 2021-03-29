#Longitude from 0-3
#Latitude from 0-3

class Board:

    def __init__(self):
        self.orgTable = []
        self.curTable = [[],[],[],[]]
        self.goalTable = []

    def makeBoard(self,filename):
        count = 1
        for line in open(filename,'r',encoding="utf-8"):
            '''up to an certain # of lines, make initial board'''
            if count >= 1 and count<= 4:
                st = line.split()
                (self.orgTable).append(st)
                
            '''up to an certain # of lines, make goal board'''
            if count >= 6 and count<= 9:
                st = line.split()
                (self.goalTable).append(st)
            count += 1
        self.curTable = self.orgTable

    def printBoard(self,letter):
        if letter == "o" or letter == "O":
            board=self.orgTable
        elif letter == "c" or letter == "C":
            board=self.curTable
        else:
            board = self.goalTable

        for ele in board:
            print(*ele)
    
    
    def makeMove(self, currLon,currLat,nextLon,nextLat):
        temp = self.curTable[currLat][currLon]
        self.curTable[currLat][currLon]= self.curTable[nextLat][nextLon]
        self.curTable[nextLat][nextLon] = temp
        

    # def heuristicAlgo(self):
    #     continue

    
