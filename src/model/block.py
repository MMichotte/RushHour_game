
class Block:
    def __init__(self, size, color, orientation, position):
        self.defaultSize = 40
        self.size = size
        self.color = color
        self.orientation = orientation
        self.position = [p * self.defaultSize for p in position]

        if self.orientation == "H":
            self.width = self.position[0] + self.size * self.defaultSize
            self.height = self.position[1] + self.defaultSize
        else:
            self.height = self.position[1] + self.size * self.defaultSize
            self.width = self.position[0] + self.defaultSize