
user = None

class User:
    def __init__(self, name):
        global user
        self.name = name
        self.score = 0
        self.currentLvl = 0
        user = self

    def __repr__(self):
        return repr('Name :' + self.name)


def getScore():
    return user.score

def setScore(n):
    global user
    newScore = user.score + n
    if newScore < 0:
        user.score = 0
    else:
        user.score = newScore

def nextLvl():
    global user
    user.currentLvl += 1

def getCurrentLvl():
    return user.currentLvl