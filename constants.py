from enum import Enum


class CellType(Enum):
    GRASS = 1,
    MOUNTAIN = 2,
    ICE = 3,
    FOREST = 4,
    RIVER = 5,
    WATER = 6,


class MineType(Enum):
    STONE_MINE = 1,
    IRON_MINE = 2,
    DIAMOND_MINE = 3,
    LOG_MINE = 4,
    FOOD_MINE = 5,
    BIG_FOOD_MINE = 6,


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN_L = (0, 255, 0)
    GREEN_D = (0, 105, 0)
    RED = (255, 0, 0)
    BLUE = (0, 255, 255)
    GREY = (105, 105, 105)
    BLUE_D = (0, 0, 128)
    BLUE_L = (176, 196, 222)


Tile_Color = {
    CellType.GRASS: Color.GREEN_L,
    CellType.MOUNTAIN: Color.GREY,
    CellType.ICE: Color.BLUE_L,
    CellType.FOREST: Color.GREEN_D,
    CellType.RIVER: Color.BLUE,
    CellType.WATER: Color.BLUE_D
    }

