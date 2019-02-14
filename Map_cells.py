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

        self.column_index = i
        self.row_index = j
        self.x_screen = self.column_index * self.cell_width
        self.y_screen = self.row_index * self.cell_height
        self.cell_type = cell_type

        if self.cell_type == CellType.GRASS:
            self.height = 1
            self.EnergyNeeded = 1
        if self.cell_type == CellType.MOUNTAIN:
            self.height = 2
            self.EnergyNeeded = 2
        if self.cell_type == CellType.ICE:
            self.height = 1
            self.EnergyNeeded = 1
        if self.cell_type == CellType.FOREST:
            self. height = 1
            self.EnergyNeeded = randint(1, 3)
        if self.cell_type == CellType.RIVER:
            self.height = 0
            self. EnergyNeeded = 2
        if self.cell_type == CellType.WATER:
            self.height = 0
            self.EnergyNeeded = 20

    def check_pos_in(self, map_i, map_j):
        return map_i == self.row_index and map_j == self.column_index

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            Tile_Color[self.cell_type],
            [self.x_screen + self.x_margin, self.y_screen + self.y_margin, self.cell_width, self.cell_height])

    @classmethod
    def create_instance(cls, cell_type, i, j, x_offset, y_offset):
        cell = cls(cell_type, i, j, x_offset, y_offset)
        return cell

    @classmethod
    def find_instance(cls, celllist, i, j):
        for row in celllist:
            for elem in row:
                if(elem.check_pos_in(i, j) == True):
                    return elem
        return None




