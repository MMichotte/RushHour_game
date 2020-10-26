from tkinter import *
from controller.blockController import BlockController
from model.block import addBlock

class BlockView:

    def __init__(self, parent, block):
        self.parentCanvas = parent
        self.blockModel = block
        
        self.blockView = self.parentCanvas.create_rectangle(self.blockModel.initialPosition[0],self.blockModel.initialPosition[1],self.blockModel.width,self.blockModel.height,fill=self.blockModel.color)
        self.blockController = BlockController(self.parentCanvas,self.blockView, self.blockModel)
        addBlock(self.blockView)

    