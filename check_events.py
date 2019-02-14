import sys
import pygame
import settings
from board import Board
from map_cells import Cell


def event_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('hi')
            check_keydown(event)


def check_keydown(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(mouse_x, mouse_y)
        Cell = Cell.find_instance(convert_screen_xy_to_map_pos(mouse_x, mouse_y))
        print(Cell)


def convert_screen_xy_to_map_pos(x, y):
    map_pos_i = x / cell_size[0]
    map_pos_j = y / cell_size[1]
    return map_pos(map_pos_i,map_pos_j)
