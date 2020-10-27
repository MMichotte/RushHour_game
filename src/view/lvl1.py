from tkinter import *
from model.block import Block

class Lvl1:
    def __init__(self, parent):
        self.parent = parent
        self.parent.update()
        self.parentW = self.parent.winfo_width()
        self.parentH = self.parent.winfo_height()-50
        self.gameW = 450
        self.gameH = self.gameW
        self.borderWidth = 5
        self.gameInteriorSize = self.gameW-2*self.borderWidth #must be devidable by numberOfLines

        self.numberOfLines= 6
        self.blockWidth = self.gameInteriorSize/self.numberOfLines
    
        self.canvas = Canvas(self.parent, width=self.gameW, height=self.gameH, bg="yellow")
        self.canvas.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2)

        self.boder = self.canvas.create_line(
            self.gameW,self.gameH/2-self.blockWidth,self.gameW,0+self.borderWidth,
            0+self.borderWidth,0+self.borderWidth,
            0+self.borderWidth,self.gameH,
            self.gameW,self.gameH,
            self.gameW,self.gameH/2,width=self.borderWidth,tags="border"
        )
        
        for l in range(self.numberOfLines):
            self.canvas.create_line(0,self.borderWidth+l*self.blockWidth,self.gameW,self.borderWidth+l*self.blockWidth)
            self.canvas.create_line(self.borderWidth+l*self.blockWidth,0,self.borderWidth+l*self.blockWidth,self.gameW)

        self.block_0 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[1,2],color="red", isMain=True)

        self.block_2 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[0,0],color="green")
        self.block_3 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[0,1],color="purple")
        self.block_4 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[0,4],color="orange")
        self.block_5 = Block(self.canvas,width=self.blockWidth,size=3,orientation="H",position=[2,5],color="green")
        self.block_6 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[3,1],color="blue")
        self.block_7 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[5,0],color="orange")
        self.block_8 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[4,4],color="lightBlue")