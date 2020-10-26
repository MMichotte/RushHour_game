from tkinter import *
from model.block import Block
from view.blockView import BlockView

class Lvl1:
    def __init__(self, parent, user):
        self.user = user

        parent.update()
        self.parentW = parent.winfo_width()
        self.parentH = parent.winfo_height()

        self.canvas = Canvas(parent, width=self.parentW-7, height=self.parentH-55, bg="yellow")
        self.canvas.place(x=0,y=0)

        self.title = self.canvas.create_text(self.parentW/2, 100, text="LvL 1")
        self.score = self.canvas.create_text(self.parentW/2, 120, text=str(self.user.getScore()))


        self.block_1_View = BlockView(self.canvas,Block(size=2,color="blue",orientation="H",position=[2,3]))
        self.block_2_View = BlockView(self.canvas,Block(size=3,color="red",orientation="V",position=[3,4]))