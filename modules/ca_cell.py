from cell import Cell


class CaCell(Cell):
    time_now = 0
    time_next = 1

    @staticmethod
    def tick():
        CaCell.time_now, CaCell.time_next = CaCell.time_next = CaCell.time_now

    @staticmethod
    def new_ca_cell(x, y):
        return CaCell(x, y)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.state = [0, 0]
