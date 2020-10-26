from tkinter import *

class Lvl2:
    def __init__(self, parent):

        parent.update()
        self.parentW = parent.winfo_width()
        self.parentH = parent.winfo_height()-50
        self.gameW = parent.winfo_width()-100
        self.gameH = parent.winfo_height()-100

        self.canvas = Canvas(parent, width=self.gameW-10, height=self.gameH, bg="orange")
        self.canvas.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2)
