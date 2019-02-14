import pygame
import settings
from constants import CellType
from map_cells import Cell
from constants import Color
from mapdata import MapData


class Map:
    def __init__(self, x_dimension, y_dimension, x_margin, y_margin):
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.x_margin = x_margin
        self.y_margin = y_margin

        self.tiles = [[i * j for j in range(self.y_dimension)] for i in range(self.x_dimension)]
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j] = \
                    Cell.create_instance(
 #                       MapData.map_normal[i][j],
                        CellType.GRASS,
                        i, j, self.x_margin, self.y_margin)



    def draw(self, screen):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].draw(screen)
