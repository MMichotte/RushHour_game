from tkinter import *
from model.user import *
from controller.levelsController import displayLvl, setParent

class MainApplication:
    def __init__(self, parent):
        parent.update()
        self.parentW = parent.winfo_width()
        self.parentH = parent.winfo_height()

        self.canvas = Canvas(parent, width=self.parentW, height=self.parentH)
        self.canvas.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2)

        self.Title = self.canvas.create_text(self.parentW/2,self.parentH/2-150,text="Rush Hour", font=("Purisa", 65), fill="green")

        self.Username = Label(self.canvas, text="Username : ", font=("Purisa", 20))
        self.Username.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2-20)
        self.UsernameEntry = Entry(self.canvas,font=("Purisa", 20))
        self.UsernameEntry.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2+20)

        self.startBtn = Button(self.canvas, text ="START", font=("Purisa", 20), width=10,command = lambda: self.startGame())
        self.startBtn.place(anchor=CENTER,x=self.parentW/2,y=self.parentH/2+150)


    def startGame(self):
        usName = Entry.get(self.UsernameEntry)
        if (usName != ""):
            self.user = User(usName)
            nextLvl()
            setParent(self.canvas)
            displayLvl(getCurrentLvl())
            
            




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