from view.levels.lvl1 import Lvl1
from view.levels.lvl2 import Lvl2
from view.levels.lvl3 import Lvl3
from view.levels.lvl4 import Lvl4
lvl = None
parent = None


def setParent(p):
    global parent
    parent = p


def displayLvl(n):
    global lvl
    if n == 1:
        clearLvl()
        lvl = Lvl1(parent)
    if n == 2:
        clearLvl()
        lvl = Lvl2(parent)
    if n == 3:
        clearLvl()
        lvl = Lvl3(parent)
    if n == 4:
        clearLvl()
        lvl = Lvl4(parent)

def clearLvl():
    global lvl
    try:
        lvl.canvas.delete('all')
        lvl.canvas.destroy()
    except Exception as e:
        #print(e)
        pass

