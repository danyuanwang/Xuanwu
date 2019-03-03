from pygame.sprite import Sprite


class MapObject(Sprite):
    def __init__(self):
        super(MapObject, self).__init__()
        self.cell = None
        self.image = None
        self.image_rect = None
        self.mine_type = None
        self.image_path = None

    def draw(self, rect, screen):
        self.image_rect = self.image.get_rect()
        rect_centerx, rect_centery = rect.get_center_point()
        # rect_centery = rect[1] + (rect[3] / 2)
        self.image_rect.centerx = rect_centerx
        self.image_rect.centery = rect_centery
        screen.blit(self.image, self.image_rect)
        # print('centerx:', rect_centerx, 'centery', rect_centery, 'minetype', self.mine_type)


