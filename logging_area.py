from constants import CellType, MineType
from mines import Mine
import pygame


class ForestMines(Mine):
    def __init__(self):
        self.miners_allowed = 0

    @classmethod
    def create_instance(cls, cell, mine_type):
        if cell.cell_type == CellType.FOREST:
            if mine_type == MineType.LOG_MINE:
                mine = LogMine()
                cell.set_mine(mine)
            if mine_type == MineType.BIG_LOG_MINE:
                mine = BigLogMine()
                cell.set_mine(mine)

            return mine
        return None


class LogMine(ForestMines):
    def __init__(self):
        self.miners_allowed = 5
        self.mine_type = MineType.LOG_MINE
        self.image_path = 'icons_and_pictures/logging_area.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))


class BigLogMine(ForestMines):
    def __init__(self):
        self.miners_allowed = 20
        self.mine_type = MineType.LOG_MINE
        self.image_path = 'icons_and_pictures/big_logging_area.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
