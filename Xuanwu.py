
import pygame
from board import Board
import settings


def run_game():
    pygame.init()
    board = Board()
    pygame.display.set_caption(settings.screen_name)
    while True:
        board.event_check()
        board.draw_board()
        pygame.display.flip()


run_game()
