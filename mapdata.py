from constants import CellType


class MapData:
    map_normal = [
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.RIVER, CellType.FOREST, CellType.FOREST, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.WATER, CellType.ICE],
        [CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.ICE, CellType.WATER, CellType.WATER, CellType.GRASS, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.RIVER, CellType.RIVER, CellType.FOREST, CellType.FOREST, CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.WATER, CellType.WATER, CellType.WATER, CellType.GRASS, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.RIVER, CellType.RIVER, CellType.FOREST, CellType.ICE, CellType.WATER, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.WATER, CellType.WATER, CellType.WATER, CellType.GRASS, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.RIVER, CellType.RIVER, CellType.ICE, CellType.ICE, CellType.ICE, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.ICE, CellType.MOUNTAIN, CellType.ICE, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.RIVER, CellType.ICE, CellType.ICE, CellType.ICE, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.ICE, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.GRASS, CellType.FOREST, CellType.RIVER, CellType.RIVER, CellType.ICE, CellType.ICE, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.GRASS, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.FOREST, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.GRASS, CellType.ICE, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.ICE, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.RIVER, CellType.RIVER, CellType.RIVER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.RIVER, CellType.GRASS, CellType.GRASS, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.RIVER, CellType.GRASS, CellType.GRASS, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.ICE, CellType.MOUNTAIN, CellType.GRASS, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.GRASS, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.WATER, CellType.WATER, CellType.ICE, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.GRASS, CellType.GRASS, CellType.RIVER, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.WATER, CellType.WATER, CellType.WATER, CellType.ICE, CellType.ICE, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.MOUNTAIN, CellType.MOUNTAIN, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER],
        [CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER, CellType.WATER]
    ]
