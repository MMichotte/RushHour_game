from view.blockView import BlockView
from controller.blockController import BlockController

blocks = []

class Block:
    def __init__(self, baseSettings, size, orientation, position, color, isMain=False):
        self.baseSettings = baseSettings
        self.defaultSize = self.baseSettings[1] #width
        self.parent = self.baseSettings[0] #parent
        self.size = size
        self.orientation = orientation
        self.position = position
        self.initialPosition = [(p * self.defaultSize) for p in self.position]
        self.color = color
        self.isMain = isMain

        if self.orientation == "H":
            self.width = self.initialPosition[0] + self.size * self.defaultSize
            self.height = self.initialPosition[1] + self.defaultSize
        else:
            self.height = self.initialPosition[1] + self.size * self.defaultSize 
            self.width = self.initialPosition[0] + self.defaultSize 

        self.addBlock(self)
        self.blockView = BlockView(self.parent, block=self)
        self.view = self.blockView.view
        self.controller = BlockController(self.parent, block=self)
        

    def addBlock(self,block):
        global blocks
        blocks.append(block)

    def getBlocks(self):
        global blocks
        return blocks

def purgeBlocks():
    global blocks
    blocks = []

def resetPositions():
    global blocks
    oldBlocks = blocks.copy()
    newBlocks = []
    for b in oldBlocks:
        newBlocks.append(
            Block(
                b.baseSettings,
                b.size,
                b.orientation,
                b.position,
                b.color,
                b.isMain
            )
        )
        b.blockView.deleteBlock()
    blocks = newBlocks.copy()
