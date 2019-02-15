import pygame
import settings
from constants import CellType
from Map_cells import Cell
from constants import Color
from mapdata import MapData


class Map:
    def __init__(self, x_dimension, y_dimension, x_margin, y_margin):
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.x_margin = x_margin
        self.y_margin = y_margin

        self.tiles = [[i_row * j_column for j_column in range(self.x_dimension)]for i_row in range(self.y_dimension)]
        for i_row in range(len(self.tiles)):
            for j_column in range(len(self.tiles[i_row])):
                print("map_normal dimension:", len(MapData.map_normal), "tiles dimension:", len(self.tiles), len(self.tiles[i_row]), "x_dimension:", x_dimension, "y_dimension:",y_dimension, "i:",i_row,"j:",j_column)
                print('x', )
                self.tiles[i_row][j_column] = \
                    Cell.create_instance(
                        MapData.map_normal[i_row][j_column],
                        i_row, j_column, self.x_margin, self.y_margin)



    def draw(self, screen):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].draw(screen)

    def find_cell_by_pos(self, i, j):
        if(i >= 0 and i < self.x_dimension and j >= 0 and j < self.y_dimension):
            return self.tiles[i][j]
        return None
