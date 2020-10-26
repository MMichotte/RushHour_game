from view.lvl1 import Lvl1
from view.lvl2 import Lvl2

class LevelsController:
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user
        self.lvl = ""

    def displayLvl(self,n):
        if n == 1:
            self.clearLvl()
            self.lvl = Lvl1(self.parent)
        if n == 2:
            self.clearLvl()
            self.lvl = Lvl2(self.parent)

    def clearLvl(self):
        try:
            self.lvl.canvas.delete('all')
            self.lvl.canvas.destroy()
        except Exception as e:
            print(e)
            pass