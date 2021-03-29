# Longitude from 0-3
# Latitude from 0-3

class Board:

    def __init__(self):
        self.curTable = []
        self.goalTable = []
        self.lat = 0
        self.lon = 0

    def makeBoard(self, filename):
        count = 1
        self.curTable = []
        self.goalTable = []
        for line in open(filename, 'r'):
            '''up to an certain # of lines, make initial board'''
            if 1 <= count <= 4:
                st = line.split()
                self.curTable.append(st)
            '''up to an certain # of lines, make goal board'''
            if 6 <= count <= 9:
                st = line.split()
                self.goalTable.append(st)
            count += 1

        for lat in range(3):
            for lon in range(3):
                if self.curTable[lat][lon] == "0":
                    self.lat = lat
                    self.lon = lon

    def printBoard(self):
        for ele in self.curTable:
            print(*ele)


    def moveUp(self):
        if self.lat == 0:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat-1][self.lon]
        self.curTable[self.lat - 1][self.lon] = "0"
        self.lat -= 1
        return True

    def moveUpRight(self):
        if self.lat == 0 or self.lon == 3:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat-1][self.lon+1]
        self.curTable[self.lat - 1][self.lon+1] = "0"
        self.lat -= 1
        self.lon += 1
        return True

    def moveRight(self):
        if self.lon == 3:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat][self.lon+1]
        self.curTable[self.lat][self.lon+1] = "0"
        self.lon += 1
        return True

    def moveRightDown(self):
        if self.lat == 3 or self.lon == 3:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat+1][self.lon+1]
        self.curTable[self.lat+1][self.lon+1] = "0"
        self.lat += 1
        self.lon += 1
        return True

    def moveDown(self):
        if self.lat == 3:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat+1][self.lon]
        self.curTable[self.lat+1][self.lon] = "0"
        self.lat += 1
        return True

    def moveDownLeft(self):
        if self.lat == 3 or self.lon == 0:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat+1][self.lon-1]
        self.curTable[self.lat+1][self.lon-1] = "0"
        self.lat += 1
        self.lon -= 1
        return True

    def moveLeft(self):
        if self.lon == 0:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat][self.lon-1]
        self.curTable[self.lat][self.lon-1] = "0"
        self.lon -= 1
        return True

    def moveLeftUp(self):
        if self.lat == 0 or self.lon == 0:
            return False
        self.curTable[self.lat][self.lon] = self.curTable[self.lat-1][self.lon-1]
        self.curTable[self.lat-1][self.lon-1] = "0"
        self.lat -= 1
        self.lon -= 1
        return True

    def heuristicAlgo(self):
        totDis = 0
        for lat1 in range(4):
            for lon1 in range(4):
                for lat2 in range(4):
                    for lon2 in range(4):
                        if self.curTable[lat1][lon1] == self.goalTable[lat2][lon2]:
                            totDis += abs(lat1-lat2) + abs(lon1-lon2)
        return totDis

    def atGoal(self):
        for lat in range(4):
            for lon in range(4):
                if not self.curTable[lat][lon] == self.goalTable[lat][lon]:
                    return False
        return True