from tkinter import *
from model.block import Block
from view.levelConstructor import LevelConstructor

class Lvl2:
    def __init__(self, parent):
        self.baseLvl = LevelConstructor(parent,6,2)
        self.canvas = self.baseLvl.getCanvas()
        self.blockWidth = self.baseLvl.getBlockWidth()

        self.blockBaseSettings = [self.canvas,self.blockWidth]

        self.block_0 = Block(self.blockBaseSettings, size=2, orientation="H", position=[0, 2], color="red", isMain=True)
        self.block_2 = Block(self.blockBaseSettings, size=3, orientation="H", position=[0, 0], color="black")
        self.block_3 = Block(self.blockBaseSettings, size=2, orientation="H", position=[0, 4], color="orange")
        self.block_4= Block(self.blockBaseSettings, size=3, orientation="V", position=[5, 1], color="gold")
        self.block_5 = Block(self.blockBaseSettings, size=2, orientation="V", position=[3, 1], color="green")
        self.block_6 = Block(self.blockBaseSettings, size=2, orientation="H", position=[3, 3], color="lightBlue")
        self.block_7 = Block(self.blockBaseSettings, size=2, orientation="V", position=[2, 3], color="maroon1")
        self.block_8 = Block(self.blockBaseSettings, size=3, orientation="H", position=[3, 5], color="purple")
        self.block_8 = Block(self.blockBaseSettings, size=3, orientation="V", position=[4, 0], color="navy")

