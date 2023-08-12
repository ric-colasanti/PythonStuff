class Grid:
    def __int__(self, size, new_function):
        self.size = size
        self.cells = []

        for i in range(self.size * self.size):
            x = i % self.size
            y = i // self.size
            self.cells.append(new_function(x, y))

        def bounds(v):
            if v < 0:
                return v + size
            if v >= size:
                return size - v
            return v

        for x in range(self.size):
            for y in range(self.size):
                i = (size * y) + x
                cell = self.cells[i]
                for yy in range(y - 1, y + 2):
                    for xx in range(x - 1, x + 2):
                        yy = bounds(yy)
                        xx = bounds(xx)
                        i_neighbour = (size * yy) + xx
                        cell_neighbour = self.cells[i_neighbour]
                        cell.add_neighbour(cell_neighbour)
