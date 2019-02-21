from pygame.sprite import Sprite
from constants import CellType, MineType
import pygame

class Mine(Sprite):
    def __init__(self, miners_allowed):
        super(Mine, self).__init__()
        self.miners_allowed = miners_allowed
        self.cell = None
        self.image = None
        self.image_rect = None

    def draw(self, rect):
        while False:
            return None

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


class StoneMine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)

    def draw(self, rect):
        self.image = pygame.image.load('icons_and_pictures/stone_mine.PNG')
        self.image_rect = self.image.get_rect()
        rect_centerx = rect[0] + (rect[2] / 2)
        rect_centery = rect[1] + (rect[3] / 2)
        self.image_rect.centerx = rect_centerx
        self.image_rect.centery = rect_centery


class IronMine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)

    def draw(self, rect):
        self.image = pygame.image.load('icons_and_pictures/iron_mine.PNG')
        self.image_rect = self.image.get_rect()
        rect_centerx = rect[0] + (rect[2]/2)
        rect_centery = rect[1] + (rect[3]/2)
        self.image_rect.centerx = rect_centerx
        self.image_rect.centery = rect_centery


class DiamondMine(Mine):
    def __init__(self):
        Mine.__init__(self, miners_allowed=3)

    def draw(self, rect):
        self.image = pygame.image.load('icons_and_pictures/diamond_mine.PNG')
        self.image_rect = self.image.get_rect()
        rect_centerx = rect[0] + (rect[2] / 2)
        rect_centery = rect[1] + (rect[3] / 2)
        self.image_rect.centerx = rect_centerx
        self.image_rect.centery = rect_centery
