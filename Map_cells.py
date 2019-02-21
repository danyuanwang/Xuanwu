import pygame
import settings
from random import randint
from constants import CellType
from constants import Color
from constants import Tile_Color


class Cell:
    def __init__(self, cell_type, i, j, x_offset, y_offset):
        self.cell_width = settings.cell_size[0]
        self.cell_height = settings.cell_size[1]
        self.x_margin = settings.cell_size[2]
        self.y_margin = settings.cell_size[3]
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.column_index = j
        self.row_index = i
        self.x_screen = self.column_index * (self.cell_width + self.x_margin) + self.x_offset
        self.y_screen = self.row_index * (self.cell_height + self.y_margin) + self.y_offset
        self.cell_type = cell_type
        self.mine = None

        if self.cell_type == CellType.GRASS:
            self.altitude = 1
            self.cross_energy = 1
        elif self.cell_type == CellType.MOUNTAIN:
            self.altitude = 2
            self.cross_energy = 2
        elif self.cell_type == CellType.ICE:
            self.altitude = 1
            self.cross_energy = 1
        elif self.cell_type == CellType.FOREST:
            self.altitude = 1
            self.cross_energy = randint(1, 3)
        elif self.cell_type == CellType.RIVER:
            self.altitude = 0
            self.cross_energy = 2
        elif self.cell_type == CellType.WATER:
            self.altitude = 0
            self.cross_energy = 20

    def check_pos_in(self, map_i, map_j):
        return map_i == self.row_index and map_j == self.column_index

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            Tile_Color[self.cell_type],
            [self.x_screen, self.y_screen, self.cell_width, self.cell_height])
        if self.mine is not None:
            rect = [self.x_screen,self.y_screen,self.cell_width,self.cell_height]
            self.mine.draw(rect)

    def check_screen_xy_in(self, screen_x, screen_y):
        if screen_x >= self.x_screen and screen_x < self.x_screen + self.cell_width:
            if screen_y >= self.y_screen and screen_y < self.y_screen + self.cell_height:
                return True
        return False
    def set_mine(self, mine):
        self.mine = mine
    @classmethod
    def create_instance(cls, cell_type, i, j, x_offset, y_offset):
        cell = cls(cell_type, i, j, x_offset, y_offset)
        return cell






