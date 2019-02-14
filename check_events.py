import sys
import pygame
from board import Board
from Map_cells import Cell
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
        Cell = find_cell(mouse_x, mouse_y)
        cell_value = check_block_click(Cell)
        print(cell_value)
def check_block_click(Cell):
    if Cell is not None:
        return Cell.return_value()
def find_cell(mouse_x, mouse_y):
    for i in range(len(Board.tiles)):
        for j in range(len(Board.tiles[i])):
            if Board.tiles[i][j].check_mouse_in(mouse_x, mouse_y):
                return Board.tiles[i][j]
    return None