from tkinter import *
from controller.timer import Timer
import model.block

timer = None

class LevelConstructor:

    def __init__(self, parent, lines, lvl ):
        global timer

        self.parent = parent
        self.numberOfLines = lines
        self.currentLvl = lvl
    
        self.parent = parent
        self.parent.update()
        self.parentW = self.parent.winfo_width()
        self.parentH = self.parent.winfo_height()-50
        self.gameW = 450
        self.gameH = self.gameW
        self.borderWidth = 5
        self.gameInteriorSize = self.gameW-2*self.borderWidth #must be dividable by numberOfLines

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

        self.statusBar = Canvas(self.parent, width=self.gameW, height=70, bg="white")
        self.statusBar.place(anchor=CENTER,x=self.parentW/2,y=self.parentH-10)

        self.resetBtn = Button(self.statusBar, text ="RESET", font=("Purisa", 20), width=10, command = model.block.resetPositions)
        self.resetBtn.place(anchor=CENTER,x=self.gameW/2,y=35)
        
        self.timerIndicator = self.statusBar.create_text(
            self.gameW-50,
            35,
            fill="black",
            font="Times 30 bold",
            text="00:00"
            )
            
        self.lvlIndicator = self.statusBar.create_text(
            50,
            35,
            fill="black",
            font="Times 30 bold",
            text="Lvl : " + str(self.currentLvl)
            )

        timer = Timer(self.statusBar,self.timerIndicator)
        timer.startTimer()

        self.canvas.bind("<Destroy>", lambda event : self.onDestroy())

    def onDestroy(self):
        global timer
        try:
            self.statusBar.destroy()
            timer.stopTimer()
        except Exception as e:
            #print(e)
            pass

    def getCanvas(self):
        return self.canvas
    
    def getBlockWidth(self):
        return self.blockWidth

def stopTimer():
    global timer
    try:
        timer.stopTimer()
    except Exception as e:
        #print(e)
        pass