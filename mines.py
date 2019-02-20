
from constants import CellType, MineType


class Mine:
    def __init__(self, miners_allowed):
        self.miners_allowed = miners_allowed
        self.cell = None

    def attach_to_cell(self, cell):
        self.cell = cell

    @classmethod
    def create_instance(cls, cell, mine_type):
        if cell.cell_type == CellType.MOUNTAIN:
            if mine_type == MineType.STONE_MINE:
                mine = Stone_Mine()
                mine.attach_to_cell(cell)
            elif mine_type == MineType.IRON_MINE:
                mine = Iron_Mine()
                mine.attach_to_cell(cell)
            elif mine_type == MineType.DIAMOND_MINE:
                mine = Diamond_Mine()
                mine.attach_to_cell(cell)
            return mine
        return None


class Stone_Mine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)


class Iron_Mine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)


class Diamond_Mine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)
