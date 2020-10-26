from model.block import getBlocks, purgeBlocks

class BlockController:

    def __init__(self,parent, blockView, block):
        self.parent = parent
        self.blockView = blockView
        self.block = block
        self.parent.tag_bind(self.blockView, "<Button-1>", self.activate)
        self.parent.tag_bind(self.blockView, "<ButtonRelease-1>", self.de_activate)
        self.parent.tag_bind(self.blockView, "<B1-Motion>", self.move)
        self.currentX = 0
        self.currentY = 0
        self.isActivated = False
    
    def activate(self, event):
        self.currentX = event.x
        self.currentY = event.y
        self.isActivated = True

    def de_activate(self, event):
        self.isActivated = False

    def move(self, event):
        if self.isActivated:
            authorizedMovements = self.checkColision()
            dx = event.x - self.currentX 
            dy = event.y - self.currentY
            if self.block.orientation == "H":  
                if dx < 0 and "R" not in authorizedMovements:
                    pass
                elif dx > 0 and "L" not in authorizedMovements:
                    pass
                else:
                    self.parent.move(self.blockView, dx, 0)
            else:
                if dy < 0 and "T" not in authorizedMovements:
                    pass
                elif dy > 0 and "B" not in authorizedMovements:
                    pass
                else:
                    self.parent.move(self.blockView, 0, dy)
            self.currentX = event.x
            self.currentY = event.y

    def checkColision(self):
        authorizedMovements = ""
        thisCoords = self.parent.bbox(self.blockView)
        if self.block.orientation == "H":
            thisCoordsA = [thisCoords[0],thisCoords[1]+(thisCoords[3]-thisCoords[1])/2] #milieu gauche
            thisCoordsB = [thisCoords[2],thisCoords[1]+(thisCoords[3]-thisCoords[1])/2] #milieu droite
            authorizedMovements = "LR"
            for b in getBlocks():
                if self.blockView != b:
                    otherCoords = self.parent.bbox(b)
                    if thisCoordsA[1] in range(otherCoords[1],otherCoords[3]):
                        if thisCoordsA[0] in range(otherCoords[0],otherCoords[2]):
                            authorizedMovements = "L"
                        if thisCoordsB[0] in range(otherCoords[0],otherCoords[2]):
                            authorizedMovements = "R"

        else:
            thisCoordsA = [thisCoords[0] + (thisCoords[2]-thisCoords[0])/2, thisCoords[1]] #milieu haut
            thisCoordsB = [thisCoords[0] + (thisCoords[2]-thisCoords[0])/2, thisCoords[3]] #milieu bas
            authorizedMovements = "TB"
            for b in getBlocks():
                if self.blockView != b:
                    otherCoords = self.parent.bbox(b)
                    if thisCoordsA[0] in range(otherCoords[0],otherCoords[2]):
                        if thisCoordsA[1] in range(otherCoords[1],otherCoords[3]):
                            authorizedMovements = "B"
                        if thisCoordsB[1] in range(otherCoords[1],otherCoords[3]):
                            authorizedMovements = "T"
        
        return authorizedMovements