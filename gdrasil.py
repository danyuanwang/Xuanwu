from map_object import MapObject
import pygame


class Shop(MapObject):
    @classmethod
    def create_instance(cls, cell):
        mine = gdrasil()
        cell.set_mine(mine)
        print('gdrasil')


class gdrasil(Shop):
    def __init__(self):
        self.image_path = 'icons_and_pictures/gdrasil.PNG'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (45, 45))

