from tkinter import *

class Lvl2:
    def __init__(self, parent, user):
        self.user = user
        self.user.setScore(-35)

        parent.update()
        self.parentW = parent.winfo_width()
        self.parentH = parent.winfo_height()-50
        self.gameW = parent.winfo_width()-100
        self.gameH = parent.winfo_height()-100

        self.canvas = Canvas(parent, width=self.gameW-10, height=self.gameH, bg="orange", highlightthickness=1, highlightbackground="black")
        self.canvas.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2)

        self.title = self.canvas.create_text(self.gameW/2, 100, text="LvL 2")
        self.score = self.canvas.create_text(self.gameW/2, 120, text=str(self.user.getScore()))
    