from tkinter import *
from model.block import Block
from view.levelConstructor import LevelConstructor

class Lvl1:
    def __init__(self, parent):

        self.baseLvl = LevelConstructor(parent,6)
        self.canvas = self.baseLvl.getCanvas()
        self.blockWidth = self.baseLvl.getBlockWidth()

        self.block_0 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[1,2],color="red", isMain=True)

        self.block_2 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[0,0],color="green")
        self.block_3 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[0,1],color="purple")
        self.block_4 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[0,4],color="orange")
        self.block_5 = Block(self.canvas,width=self.blockWidth,size=3,orientation="H",position=[2,5],color="green")
        self.block_6 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[3,1],color="blue")
        self.block_7 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[5,0],color="orange")
        self.block_8 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[4,4],color="lightBlue")