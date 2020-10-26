from tkinter import *

class Lvl2:
    def __init__(self, parent, user):
        self.user = user
        self.user.setScore(-35)

        parent.update()
        self.parentW = parent.winfo_width()
        self.parentH = parent.winfo_height()

        self.canvas = Canvas(parent, width=self.parentW-7, height=self.parentH-55, bg="orange")
        self.canvas.place(x=0,y=0)

        self.title = self.canvas.create_text(self.parentW/2, 100, text="LvL 2")
        self.score = self.canvas.create_text(self.parentW/2, 120, text=str(self.user.getScore()))
    