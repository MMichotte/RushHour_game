from tkinter import *
from view.menu import Menu
from model.user import User

class MainApplication:
    def __init__(self, parent):
        self.canvas = Canvas(parent, bg="red")
        self.canvas.pack(fill=BOTH,expand=1)
        
        self.user = User("Martin")
        
        self.menu = Menu(parent, self.user)





if __name__ == "__main__":
    width = 400
    height = 400
    size = ""+ str(width) + "x" + str(height)
    root = Tk()
    root.geometry(size)
    root.resizable(0, 0)
    MainApplication(root)
    root.mainloop()