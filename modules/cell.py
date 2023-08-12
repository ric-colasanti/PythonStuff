class Cell:

    def __init__(self, x, y):
        self.neighbours = []
        self.xPos = x
        self.yPos = y
        self.number_neighbours = -1

    def add_neighbour(self, cell):
        self.neighbours.append(cell)
        self.number_neighbours += 1
