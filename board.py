import pygame
import settings
import sys
from Map_cells import Cell
from constants import Color
from mapdata import MapData
from map import Map

class Board():

    def __init__(self):
        self.num_of_cell_X = settings.board_dimension[0]
        self.num_of_cell_Y = settings.board_dimension[1]
        self.x_margin = settings.board_dimension[2]
        self.y_margin = settings.board_dimension[3]

        self.map = Map(self.num_of_cell_X, self.num_of_cell_Y, self.x_margin, self.y_margin)

    def draw_board(self):
        screen = pygame.display.set_mode(settings.screen_size)
        screen.fill(Color.WHITE)
        self.map.draw(screen)


    def event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_keydown(event)


    def check_keydown(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #map_pos_i_row, map_pos_j_column = Map.convert_screen_xy_to_map_pos(mouse_x, mouse_y)
            #print(mouse_x, mouse_y, map_pos_i_row, map_pos_j_column)
            #cell = self.map.find_cell_by_pos(map_pos_i_row, map_pos_j_column)
            cell = self.map.find_cell_by_xy(mouse_x,mouse_y)
            if cell is not None:
                print(cell.altitude , cell.cross_energy)




