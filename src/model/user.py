
class User:
    def __init__(self, name):
        self.name = name
        self.score = 2000
        self.currentLvl = 0

    def getScore(self):
        return self.score

    def setScore(self,n):
        newScore = self.score + n
        if newScore < 0:
            self.score = 0
        else:
            self.score = newScore

    def nextLvl(self):
        self.currentLvl += 1
    
    def getCurrentLvl(self):
        return self.currentLvl

    def __repr__(self):
        return repr('Name :' + self.name)