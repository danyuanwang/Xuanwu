import pygame
import settings
from Map_cells import Cell
class Board():
    BLACK = (0, 0, 0)

    WHITE = (255, 255, 255)
    GREEN_L = (0, 255, 0)
    GREEN_D = (0, 105, 0)
    RED = (255, 0, 0)
    BLUE = (0, 255, 255)
    GREY = (105, 105, 105)
    BLUE_D = (0, 0, 128)
    BLUE_L = (176, 196, 222)

    GRASS = Cell(1)
    MOUNTAIN = Cell(2)
    ICE = Cell(3)
    FOREST = Cell(4)
    RIVER = Cell(5)
    WATER = Cell(6)
    tiles = [
        [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
        [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, ICE],
        [WATER, WATER, WATER, WATER, WATER, MOUNTAIN, MOUNTAIN, FOREST, FOREST, FOREST, RIVER, FOREST, FOREST, WATER, WATER, WATER, WATER, ICE, WATER, ICE],
        [WATER, WATER, MOUNTAIN, ICE, WATER, WATER, GRASS, MOUNTAIN, FOREST, FOREST, RIVER, RIVER, FOREST, FOREST, WATER, WATER, WATER, ICE, WATER, WATER],
        [WATER, WATER, MOUNTAIN, WATER, WATER, WATER, GRASS, MOUNTAIN, FOREST, FOREST, FOREST, RIVER, RIVER, FOREST, ICE, WATER, ICE, ICE, WATER, WATER],
        [WATER, WATER, MOUNTAIN, WATER, WATER, WATER, GRASS, MOUNTAIN, FOREST, FOREST, FOREST, RIVER, RIVER, ICE, ICE, ICE, ICE, ICE, WATER, WATER],
        [WATER, WATER, ICE, MOUNTAIN, ICE, MOUNTAIN, MOUNTAIN, FOREST, FOREST, FOREST, FOREST, FOREST, RIVER, ICE, ICE, ICE, ICE, ICE, WATER, WATER],
        [WATER, WATER, WATER, ICE, ICE, MOUNTAIN, MOUNTAIN, FOREST, FOREST, FOREST, GRASS, FOREST, RIVER, RIVER, ICE, ICE, ICE, ICE, WATER, WATER],
        [WATER, WATER, WATER, GRASS, MOUNTAIN, MOUNTAIN, FOREST, FOREST, FOREST, FOREST, GRASS, GRASS, GRASS, RIVER, GRASS, ICE, ICE, ICE, WATER, WATER],
        [WATER, WATER, WATER, ICE, ICE, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, RIVER, RIVER, RIVER, RIVER, WATER, WATER, WATER, WATER],
        [WATER, WATER, WATER, ICE, MOUNTAIN, MOUNTAIN, GRASS, GRASS, GRASS, GRASS, GRASS, RIVER, RIVER, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER],
        [WATER, WATER, WATER, WATER, ICE, MOUNTAIN, MOUNTAIN, GRASS, GRASS, GRASS, RIVER, RIVER, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER, WATER],
        [WATER, WATER, WATER, WATER, MOUNTAIN, ICE, MOUNTAIN, GRASS, GRASS, GRASS, RIVER, GRASS, MOUNTAIN, MOUNTAIN, WATER, WATER, ICE, WATER, WATER, WATER],
        [WATER, WATER, WATER, WATER, WATER, MOUNTAIN, MOUNTAIN, MOUNTAIN, GRASS, GRASS, RIVER, MOUNTAIN, MOUNTAIN, WATER, WATER, WATER, ICE, ICE, WATER, WATER],
        [WATER, WATER, WATER, WATER, WATER, WATER, MOUNTAIN, MOUNTAIN, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
        [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER]
    ]
    Tile_Color = {
        GRASS: GREEN_L,
        MOUNTAIN: GREY,
        ICE: BLUE_L,
        FOREST: GREEN_D,
        RIVER: BLUE,
        WATER: BLUE_D
        }
#    def __init__(self):



    def draw_board(self):

        for i in range(len(Board.tiles)):
            for j in range(len(Board.tiles[i])):
               Board.tiles[i][j].set_corrdinator(i, j)


        width = 50
        height = 50
        screen = pygame.display.set_mode(settings.screen_size)
        screen.fill(Board.WHITE)
        plus_amount = 10
        row_height = 7
        for row in range(16):
            for column in range(20):
                pygame.draw.rect(screen, Board.Tile_Color[Board.tiles[row][column]], [(column * 50) + plus_amount, row_height, width, height])
                plus_amount += 1
            plus_amount = 10
            row_height += 51




