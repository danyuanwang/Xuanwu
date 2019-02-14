import pygame
import settings
from map_cells import Cell
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





