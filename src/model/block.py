from view.blockView import BlockView
from controller.blockController import BlockController

blocks = []

class Block:
    def __init__(self, parent, width, size, orientation, position, color, isMain=False):
        self.defaultSize = width
        self.parent = parent
        self.size = size
        self.orientation = orientation
        self.initialPosition = [(p * self.defaultSize) for p in position]
        self.color = color
        self.isMain = isMain

        if self.orientation == "H":
            self.width = self.initialPosition[0] + self.size * self.defaultSize
            self.height = self.initialPosition[1] + self.defaultSize
        else:
            self.height = self.initialPosition[1] + self.size * self.defaultSize 
            self.width = self.initialPosition[0] + self.defaultSize 

        self.addBlock(self)
        self.view = BlockView(self.parent, block=self).view
        self.controller = BlockController(self.parent, block=self)
        

    def addBlock(self,block):
        global blocks
        blocks.append(block)

    def purgeBlocks(self):
        global blocks
        blocks = []

    def getBlocks(self):
        global blocks
        return blocks