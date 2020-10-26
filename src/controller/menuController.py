from controller.levelsController import LevelsController

class MenuController:
    def __init__(self, parent, user):
        self.user = user
        self.levelsController = LevelsController(parent,self.user)

    def loadNextLvl(self):
        self.user.nextLvl()
        self.levelsController.displayLvl(self.user.getCurrentLvl())