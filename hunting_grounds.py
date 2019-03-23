from constants import CellType, MineType
from mines import Mine
import pygame


class GrassMines(Mine):
    def __init__(self):
        self.miners_allowed = 0

    @classmethod
    def create_instance(cls, cell, mine_type):
        if cell.cell_type == CellType.GRASS:
            if mine_type == MineType.FOOD_MINE:
                mine = HuntMine()
                cell.set_mine(mine)
            if mine_type == MineType.BIG_FOOD_MINE:
                mine = BigHuntMine()
                cell.set_mine(mine)
            return mine
        return None


class HuntMine(GrassMines):
    def __init__(self):
        self.miners_allowed = 5

        self.mine_type = MineType.FOOD_MINE
        self.image_path = 'icons_and_pictures/hunting_ground.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))


class BigHuntMine(GrassMines):
    def __init__(self):
        self.miners_allowed = 15

        self.mine_type = MineType.FOOD_MINE
        self.image_path = 'icons_and_pictures/big_hunting_ground.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
