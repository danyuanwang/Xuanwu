import pygame
import settings
from constants import CellType
from Map_cells import Cell
from constants import Color
from mapdata import MapData
from mines import Mine
from random import randint
from constants import MineType

class Map:
    stone_mines_limit = randint(settings.stone_mine_number[0], settings.stone_mine_number[1])
    iron_mines_limit = randint(settings.iron_mine_number[0], settings.iron_mine_number[1])
    diamond_mines_limit = randint(settings.diamond_mine_number[0], settings.diamond_mine_number[1])
    stone_mines_list = []
    iron_mines_list = []
    diamond_mines_list = []

    def __init__(self, x_dimension, y_dimension, x_margin, y_margin):
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.x_margin = x_margin
        self.y_margin = y_margin

        self.tiles = [[i_row * j_column for j_column in range(self.x_dimension)]for i_row in range(self.y_dimension)]
        self.mountains_list = []
        for i_row in range(len(self.tiles)):
            for j_column in range(len(self.tiles[i_row])):
                #print("map_normal dimension:", len(MapData.map_normal), "tiles dimension:", len(self.tiles), len(self.tiles[i_row]), "x_dimension:", x_dimension, "y_dimension:",y_dimension, "i:",i_row,"j:",j_column)
                self.tiles[i_row][j_column] = \
                    Cell.create_instance(
                        MapData.map_normal[i_row][j_column],
                        i_row, j_column, self.x_margin, self.y_margin)
                cell = self.tiles[i_row][j_column]

                if cell.cell_type == CellType.MOUNTAIN:
                    self.mountains_list.append(cell)
                print("cell", cell.cell_type)
        for i in range(Map.stone_mines_limit + Map.iron_mines_limit + Map.diamond_mines_limit):
            index_mountain = randint(0, len(self.mountains_list)-1)
            selected_mountain_cell = self.mountains_list[index_mountain]
            if len(Map.stone_mines_list) < Map.stone_mines_limit:
                mine = Mine.create_instance(selected_mountain_cell, MineType.STONE_MINE)
                if mine is not None:
                    Map.stone_mines_list.append(mine)
            if len(Map.iron_mines_list) < Map.iron_mines_limit:
                mine = Mine.create_instance(selected_mountain_cell, MineType.IRON_MINE)
                if mine is not None:
                    Map.iron_mines_list.append(mine)
            if len(Map.diamond_mines_list) < Map.diamond_mines_limit:
                mine = Mine.create_instance(selected_mountain_cell, MineType.DIAMOND_MINE)
                if mine is not None:
                    Map.diamond_mines_list.append(mine)

        print("stone mines", Map.stone_mines_list, Map.stone_mines_limit)
        print("iron mines", Map.iron_mines_list, Map.iron_mines_limit)
        print("diamond mines", Map.diamond_mines_list, Map.diamond_mines_limit)

    def draw(self, screen):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].draw(screen)

    def find_cell_by_pos(self, i_row, j_column):
        print('i_row and j_column:', i_row, j_column, 'x and y:', self.x_dimension, self.y_dimension)
        if(i_row >= 0 and i_row < self.y_dimension and j_column >= 0 and j_column < self.x_dimension):
            return self.tiles[i_row][j_column]
        return None

    def find_cell_by_xy(self, screen_x, screen_y):
        for row in self.tiles:
            for cell in row:
                if cell.check_screen_xy_in(screen_x, screen_y):
                    return cell
        return None

    @staticmethod
    def convert_screen_xy_to_map_pos(x, y):
        cell_width = settings.cell_size[0]
        cell_height = settings.cell_size[1]
        x_margin = settings.cell_size[2]
        y_margin = settings.cell_size[3]
        x_offset = settings.board_dimension[2]
        y_offset = settings.board_dimension[3]
        map_pos_j_column = int((x - x_offset)/(cell_width + x_margin))
        map_pos_i_row = int((y - y_offset)/(cell_height + y_margin))
        return map_pos_i_row,map_pos_j_column
