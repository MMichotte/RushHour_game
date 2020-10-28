from tkinter import *
from model.block import Block
from view.levelConstructor import LevelConstructor

class Lvl2:
    def __init__(self, parent):
        self.baseLvl = LevelConstructor(parent,6)
        self.canvas = self.baseLvl.getCanvas()
        self.blockWidth = self.baseLvl.getBlockWidth()

        self.blockBaseSettings = [self.canvas,self.blockWidth]

        self.block_0 = Block(self.blockBaseSettings,size=2,orientation="H",position=[1,2],color="red", isMain=True)
        self.block_2 = Block(self.blockBaseSettings,size=3,orientation="H",position=[3,0],color="maroon1")
        self.block_3 = Block(self.blockBaseSettings,size=2,orientation="V",position=[2,0],color="green")
        self.block_4 = Block(self.blockBaseSettings,size=2,orientation="V",position=[0,1],color="grey")
        self.block_5 = Block(self.blockBaseSettings,size=2,orientation="H",position=[4,1],color="lightBlue")
        self.block_6 = Block(self.blockBaseSettings,size=3,orientation="V",position=[3,1],color="purple")
        self.block_7 = Block(self.blockBaseSettings,size=2,orientation="V",position=[1,3],color="maroon1")
        self.block_8 = Block(self.blockBaseSettings,size=2,orientation="H",position=[4,3],color="Blue")
        self.block_9 = Block(self.blockBaseSettings,size=2,orientation="V",position=[0,4],color="green")
        self.block_10 = Block(self.blockBaseSettings,size=2,orientation="V",position=[5,4],color="gold")
        self.block_11 = Block(self.blockBaseSettings,size=2,orientation="H",position=[2,4],color="black")
        self.block_12 = Block(self.blockBaseSettings,size=3,orientation="H",position=[1,5],color="navy")