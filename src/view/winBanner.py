from tkinter import *
from model.user import *
import controller.levelsController
import model.block

class WinBanner:
    def __init__(self, parent):
        self.parent = parent
        self.parent.update()
        self.bannerW = parent.winfo_width()-100
        self.bannerH = parent.winfo_height()/2

        self.rect = self.parent.create_rectangle(
            self.parent.winfo_width()/2-150,
            self.parent.winfo_height()/2-75,
            self.parent.winfo_width()/2+150,
            self.parent.winfo_height()/2+100,
            fill="white"
            )

        self.text = self.parent.create_text(
            self.parent.winfo_width()/2,
            self.parent.winfo_height()/2,
            width=self.bannerW,
            fill="red",
            font="Times 40 bold",
            text="YOU WON"
            )
        self.nextLvlBtn = Button(self.parent, text ="NEXT", font=("Purisa", 20), width=10,command = lambda: self.startNextLvl())
        self.nextLvlBtn.place(anchor=CENTER,x=self.parent.winfo_width()/2,y=self.parent.winfo_height()/2+50)

    def startNextLvl(self):
        nextLvl()
        model.block.purgeBlocks()
        controller.levelsController.displayLvl(getCurrentLvl())
