from view.levels.lvl1 import Lvl1
from view.levels.lvl2 import Lvl2

lvl = None
mainParent = None
parent = None


def setParent(p,mp):
    global parent, mainParent
    parent = p
    mainParent = mainParent

def displayLvl(n):
    if n == 1:
        clearLvl()
        lvl = Lvl1(parent)
    if n == 2:
        clearLvl()
        lvl = Lvl2(parent)

def clearLvl():
    try:
        lvl.canvas.delete('all')
        lvl.canvas.destroy()
    except Exception as e:
        #print(e)
        pass

