

blocks = []

def addBlock(block):
    global blocks
    blocks.append(block)

def purgeBlocks():
    global blocks
    blocks = []

def getBlocks():
    return blocks

class Block:
    def __init__(self, size, color, orientation, position):
        self.defaultSize = 40
        self.size = size
        self.color = color
        self.orientation = orientation
        self.initialPosition = [p * self.defaultSize for p in position]

        if self.orientation == "H":
            self.width = self.initialPosition[0] + self.size * self.defaultSize
            self.height = self.initialPosition[1] + self.defaultSize
        else:
            self.height = self.initialPosition[1] + self.size * self.defaultSize
            self.width = self.initialPosition[0] + self.defaultSize