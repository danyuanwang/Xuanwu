import pygame
import settings
class Board():
#    def __init__(self):



    def draw_board(self):
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        width = 50
        height = 50
        screen = pygame.display.set_mode(settings.screen_size)
        screen.fill(BLACK)
        plus_amount = 10
        row_height = 7
        for row in range(1, 17):
            for column in range(1, 21):
                pygame.draw.rect(screen, WHITE, [((column - 1) * 50) + plus_amount, row_height, width, height])
                plus_amount += 1
            plus_amount = 10
            row_height += 51




