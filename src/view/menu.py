from tkinter import *
from controller.menuController import MenuController

class Menu:

    def __init__(self, parent, user):
    
        self.menuController = MenuController(parent, user)
        
        parent.update()
        self.canvas = Canvas(parent, width=parent.winfo_width(), height=50, bg="green", highlightthickness=0)
        self.canvas.place(x=0,y=parent.winfo_height()-50)

        self.backBtn = Button(self.canvas, text ="back", width=10)
        self.backBtn.place(anchor=CENTER, x=(parent.winfo_width()/2)-50, y=25)
        self.nextLvlBtn = Button(self.canvas, text ="Next Level", width=10, command = lambda: self.menuController.loadNextLvl())
        self.nextLvlBtn.place(anchor=CENTER, x=(parent.winfo_width()/2)+50, y= 25)
               