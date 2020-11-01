from tkinter import *
from model.block import Block
from view.levelConstructor import LevelConstructor

class Lvl3:
    def __init__(self, parent):
        self.baseLvl = LevelConstructor(parent,6,3)
        self.canvas = self.baseLvl.getCanvas()
        self.blockWidth = self.baseLvl.getBlockWidth()

        self.blockBaseSettings = [self.canvas,self.blockWidth]

        self.block_0 = Block(self.blockBaseSettings,size=2,orientation="H",position=[0,2],color="red", isMain=True)
        self.block_2 = Block(self.blockBaseSettings, size=3, orientation="H", position=[3,5], color="green")
        self.block_3= Block(self.blockBaseSettings, size=2, orientation="H", position=[4, 3], color="lightBlue")
        self.block_4 = Block(self.blockBaseSettings, size=3, orientation="V", position=[0, 3], color="orange")
        self.block_5 = Block(self.blockBaseSettings, size=3, orientation="V", position=[5, 0], color="black")
        self.block_6 = Block(self.blockBaseSettings, size=2, orientation="V", position=[3, 2], color="blue")
        self.block_7 = Block(self.blockBaseSettings, size=3, orientation="V", position=[2, 0], color="purple")
        self.block_8 = Block(self.blockBaseSettings, size=3, orientation="H", position=[3, 4], color="maroon1")
        self.block_9 = Block(self.blockBaseSettings, size=2, orientation="H", position=[0, 0], color="navy")
        self.block_10 = Block(self.blockBaseSettings, size=2, orientation="H", position=[3, 1], color="grey")