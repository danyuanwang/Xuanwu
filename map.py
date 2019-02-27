import pygame
import settings
from constants import CellType
from Map_cells import Cell
from constants import Color
from mapdata import MapData
from mines import Mine , MountainMines
from logging_area import ForestMines
from random import randint
from constants import MineType
from hunting_grounds import GrassMines

class Map:
    stone_mines_limit = randint(settings.stone_mine_number['low_value'], settings.stone_mine_number['high_value'])
    iron_mines_limit = randint(settings.iron_mine_number['low_value'], settings.iron_mine_number['high_value'])
    diamond_mines_limit = randint(settings.diamond_mine_number['low_value'], settings.diamond_mine_number['high_value'])
    logging_mines_limit = randint(settings.logging_mine_number['low_value'], settings.logging_mine_number['high_value'])
    grass_mines_limit = randint(settings.hunting_mine_number['low_value'], settings.hunting_mine_number['high_value'])
    big_grass_mines_limit = randint(settings.big_hunting_mine_number['low_value'], settings.big_hunting_mine_number['high_value'])

    def __init__(self, x_dimension, y_dimension, x_margin, y_margin):
        self.stone_mines_list = []
        self.iron_mines_list = []
        self.diamond_mines_list = []
        self.logging_mines_list = []
        self.grass_mines_list = []
        self.big_grass_mines_list = []
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.x_margin = x_margin
        self.y_margin = y_margin
        print('stone limit:', Map.stone_mines_limit, 'list', len(self.stone_mines_list))
        print('iron limit:', Map.iron_mines_limit, 'list', len(self.iron_mines_list))
        print('diamond limit:', Map.diamond_mines_limit, 'list:', len(self.diamond_mines_list))

        self.tiles = [[i_row * j_column for j_column in range(self.x_dimension)]for i_row in range(self.y_dimension)]
        self.mountains_without_mines_list = []
        self.forests_without_mines_list = []
        self.grass_without_mines_list = []
        for i_row in range(len(self.tiles)):
            for j_column in range(len(self.tiles[i_row])):
                #print("map_normal dimension:", len(MapData.map_normal), "tiles dimension:", len(self.tiles), len(self.tiles[i_row]), "x_dimension:", x_dimension, "y_dimension:",y_dimension, "i:",i_row,"j:",j_column)
                self.tiles[i_row][j_column] = \
                    Cell.create_instance(
                        MapData.map_normal[i_row][j_column],
                        i_row, j_column, self.x_margin, self.y_margin)
                cell = self.tiles[i_row][j_column]

                if cell.cell_type == CellType.MOUNTAIN:
                    self.mountains_without_mines_list.append(cell)
                if cell.cell_type == CellType.FOREST:
                    self.forests_without_mines_list.append(cell)
                if cell.cell_type == CellType.GRASS:
                    self.grass_without_mines_list.append(cell)
                #print("cell", cell.cell_type)
        self.create_mountain_mines()
        self.create_forest_mines()
        self.create_grass_mines()



        #print("stone mines", Map.stone_mines_list, Map.stone_mines_limit)
        #print("iron mines", Map.iron_mines_list, Map.iron_mines_limit)
        #print("diamond mines", Map.diamond_mines_list, Map.diamond_mines_limit)


    def draw(self, screen):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].draw(screen)

    def find_cell_by_pos(self, i_row, j_column):
        print('i_row and j_column:', i_row, j_column, 'x and y:', self.x_dimension, self.y_dimension)
        if i_row >= 0 and i_row < self.y_dimension and j_column >= 0 and j_column < self.x_dimension:
            return self.tiles[i_row][j_column]
        return None

    def find_cell_by_xy(self, screen_x, screen_y):
        for row in self.tiles:
            for cell in row:
                if cell.check_screen_xy_in(screen_x, screen_y):
                    return cell
        return None

    def create_mountain_mines(self):
        while len(self.stone_mines_list)+len(self.iron_mines_list) + len(self.diamond_mines_list) <\
                Map.stone_mines_limit + Map.iron_mines_limit + Map.diamond_mines_limit:
            index_mountain = randint(0, len(self.mountains_without_mines_list)-1)
            selected_mountain_cell = self.mountains_without_mines_list[index_mountain]
            if selected_mountain_cell.has_mine() is not True:
                if len(self.stone_mines_list) < Map.stone_mines_limit:
                    mine = MountainMines.create_instance(selected_mountain_cell, MineType.STONE_MINE)
                    if mine is not None:
                        self.stone_mines_list.append(mine)
                        self.mountains_without_mines_list.remove(selected_mountain_cell)
                        print('made a mine', mine.mine_type, 'index', index_mountain)
            if selected_mountain_cell.has_mine() is not True:
                if len(self.iron_mines_list) < Map.iron_mines_limit:
                    mine = MountainMines.create_instance(selected_mountain_cell, MineType.IRON_MINE)
                    if mine is not None:
                        self.iron_mines_list.append(mine)
                        self.mountains_without_mines_list.remove(selected_mountain_cell)
                        print('made a mine', mine.mine_type, 'index', index_mountain)
            if selected_mountain_cell.has_mine() is not True:
                if len(self.diamond_mines_list) < Map.diamond_mines_limit:
                    mine = MountainMines.create_instance(selected_mountain_cell, MineType.DIAMOND_MINE)
                    if mine is not None:
                        self.diamond_mines_list.append(mine)
                        self.mountains_without_mines_list.remove(selected_mountain_cell)
                        print('made a mine', mine.mine_type, 'index', index_mountain)

    def create_forest_mines(self):
        while len(self.logging_mines_list) < self.logging_mines_limit:
            index_forest = randint(0, len(self.forests_without_mines_list) - 1)
            selected_forest_cell = self.forests_without_mines_list[index_forest]
            if selected_forest_cell.has_mine() is not True:
                if len(self.logging_mines_list) < Map.logging_mines_limit:
                    mine = ForestMines.create_instance(selected_forest_cell, MineType.LOG_MINE)
                    if mine is not None:
                        self.logging_mines_list.append(mine)
                        self.forests_without_mines_list.remove(selected_forest_cell)
                        print('made a mine', mine.mine_type, 'index', index_forest)

    def create_grass_mines(self):
        while len(self.grass_mines_list) + len(self.big_grass_mines_list) < self.grass_mines_limit + self.big_grass_mines_limit:
            index_grass = randint(0, len(self.grass_without_mines_list) - 1)
            selected_grass_cell = self.grass_without_mines_list[index_grass]
            if selected_grass_cell.has_mine() is not True:
                if len(self.grass_mines_list) < Map.grass_mines_limit:
                    print()
                    mine = GrassMines.create_instance(selected_grass_cell, MineType.FOOD_MINE)
                    if mine is not None:
                        self.grass_mines_list.append(mine)
                        self.grass_without_mines_list.remove(selected_grass_cell)
                        print('made a mine', mine.mine_type, 'index', index_grass)
            if selected_grass_cell.has_mine() is not True:
                if len(self.big_grass_mines_list) < Map.big_grass_mines_limit:
                    mine = GrassMines.create_instance(selected_grass_cell, MineType.BIG_FOOD_MINE)
                    if mine is not None:
                        self.big_grass_mines_list.append(mine)
                        self.grass_without_mines_list.remove(selected_grass_cell)
                        print('made a mine', mine.mine_type, 'index', index_grass)
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
