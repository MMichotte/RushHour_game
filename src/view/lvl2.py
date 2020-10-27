from tkinter import *
from model.block import Block

class Lvl2:
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

        self.block_2 = Block(self.canvas,width=self.blockWidth,size=3,orientation="H",position=[3,0],color="yellow")
        self.block_3 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[2,0],color="green")
        self.block_4 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[0,1],color="grey")
        self.block_5 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[4,1],color="lightBlue")
        self.block_6 = Block(self.canvas,width=self.blockWidth,size=3,orientation="V",position=[3,1],color="purple")
        self.block_7 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[1,3],color="maroon1")
        self.block_8 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[4,3],color="Blue")
        self.block_9 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[0,4],color="green")
        self.block_10 = Block(self.canvas,width=self.blockWidth,size=2,orientation="V",position=[5,4],color="gold")
        self.block_11 = Block(self.canvas,width=self.blockWidth,size=2,orientation="H",position=[2,4],color="black")
        self.block_12 = Block(self.canvas,width=self.blockWidth,size=3,orientation="H",position=[1,5],color="navy")