from pygame.sprite import Sprite
from constants import CellType, MineType
import pygame
from map_object import MapObject
from random import  randint
from rectangle import Rectangle


class Mine(MapObject):
    def __init__(self):

        self.miners_allowed = 0



class MountainMines(Mine):
    def __init__(self):
        self.miners_allowed = 3

    @classmethod
    def create_instance(cls, cell, mine_type):
        if cell.cell_type == CellType.MOUNTAIN:
            if mine_type == MineType.STONE_MINE:
                mine = StoneMine()
                cell.set_mine(mine)
            elif mine_type == MineType.IRON_MINE:
                mine = IronMine()
                cell.set_mine(mine)
            elif mine_type == MineType.DIAMOND_MINE:
                mine = DiamondMine()
                cell.set_mine(mine)
            return mine
        return None


class StoneMine(MountainMines):
    def __init__(self):
        MountainMines.__init__(self)
        self.mine_type = MineType.STONE_MINE
        self.image_path = 'icons_and_pictures/stone_mine.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))


class IronMine(MountainMines):
    def __init__(self):
        MountainMines.__init__(self)
        self.mine_type = MineType.IRON_MINE
        self.image_path = 'icons_and_pictures/iron_mine.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))


class DiamondMine(MountainMines):
    def __init__(self):
        MountainMines.__init__(self)
        self.mine_type = MineType.DIAMOND_MINE
        self.image_path = 'icons_and_pictures/diamond_mine.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
