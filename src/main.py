from tkinter import *
from view.menu import Menu
from model.user import User

class MainApplication:
    def __init__(self, parent):
        
        self.user = User("Martin")
        
        self.menu = Menu(parent, self.user)





if __name__ == "__main__":
    width = 600
    height = 600
    size = ""+ str(width) + "x" + str(height)
    root = Tk()
    root.title("Rush Hour")
    root.geometry(size)
    root.resizable(0, 0)
    MainApplication(root)
    root.mainloop()