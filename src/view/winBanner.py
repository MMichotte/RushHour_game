from tkinter import *

class WinBanner:
     def __init__(self, parent):
        
        self.parent = parent

        self.parent.update()
        self.bannerW = parent.winfo_width()-100
        self.bannerH = parent.winfo_height()/2

        self.text = self.parent.create_text(
            self.parent.winfo_width()/2,
            self.parent.winfo_height()/2,
            width=self.bannerW,
            fill="red",
            font="Times 40 bold",
            text="YOU WON"
            )

        self.score = self.parent.create_text(
            self.parent.winfo_width()/2,
            self.parent.winfo_height()/2+40,
            width=self.bannerW,
            fill="red",
            font="Times 40 bold",
            text="Score :" + "TODO"
            )
