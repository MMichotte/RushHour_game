from tkinter import *
from controller.blockController import BlockController

class BlockView:
    def __init__(self, parent, block):
        self.parentCanvas = parent
        self.blockModel = block
        
        self.block = self.parentCanvas.create_rectangle(self.blockModel.position[0],self.blockModel.position[1],self.blockModel.width,self.blockModel.height,fill=self.blockModel.color)
        self.blockController = BlockController(self.parentCanvas,self.block)