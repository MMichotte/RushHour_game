
class BlockController:

    def __init__(self,parent, block):
        self.parent = parent
        self.block = block
        self.parent.tag_bind(self.block, "<Button-1>", self.activate)
        self.parent.tag_bind(self.block, "<ButtonRelease-1>", self.de_activate)
        self.parent.tag_bind(self.block, "<B1-Motion>", self.move)
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
            dx = event.x - self.currentX 
            dy = event.y - self.currentY
            self.parent.move(self.block, dx, dy)
            self.currentX = event.x
            self.currentY = event.y
