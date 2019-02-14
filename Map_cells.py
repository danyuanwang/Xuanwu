
from random import randint
class Cell():
    GRASS = 1
    MOUNTAIN = 2
    ICE = 3
    FOREST = 4
    RIVER = 5
    WATER = 6
    def __init__(self, cell_type):
        self.cell_type = cell_type
        if self.cell_type == GRASS:
            self.height = 1
            self.EnergyNeeded = 1
        if self.cell_type == MOUNTAIN:
            self.height = 2
            self.EnergyNeeded = 2
        if self.cell_type == ICE:
            self.height = 1
            self.EnergyNeeded = 1
        if self.cell_type == FOREST:
            self. height = 1
            self.EnergyNeeded = randint(1, 3)
        if self.cell_type == RIVER:
            self.height = 0
            self. EnergyNeeded = 2
        if self.cell_type == WATER:
            self.height = 0
            self. EnergyNeeded = 20
    def return_value(self):
        return self.height
        return self.EnergyNeeded
    def set_corrdinator(self, i, j):
        self.x = 50* i + i
        self.y = 50* j + j
        print("sent_cor:", self.x,self.y)
    def check_mouse_in(self, mouse_x, mouse_y):
        if mouse_x >= self.x  and mouse_x <= self.x + 50:
            if mouse_y >= self.y and mouse_y <= self.y + 50:
                return True
        print("mouse_x:", mouse_x, "mouse_y:", mouse_y)
        print("self.x:", self.x, "self.y:", self.y)
        return False
    def create_instance(type):
        return cell(type)



