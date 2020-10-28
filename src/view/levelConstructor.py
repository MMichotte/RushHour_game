from tkinter import *

class LevelConstructor:
    def __init__(self, parent, lines ):
        self.parent = parent
        self.numberOfLines = lines
    
        self.parent = parent
        self.parent.update()
        self.parentW = self.parent.winfo_width()
        self.parentH = self.parent.winfo_height()-50
        self.gameW = 450
        self.gameH = self.gameW
        self.borderWidth = 5
        self.gameInteriorSize = self.gameW-2*self.borderWidth #must be devidable by numberOfLines

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

    def getCanvas(self):
        return self.canvas
    
    def getBlockWidth(self):
        return self.blockWidth