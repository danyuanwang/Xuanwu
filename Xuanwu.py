
import pygame
from board import Board
import settings
import check_events
def run_game():
    pygame.init()
    board = Board()
    screen = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption("xuanwu game")
    while True:
        check_events.exit_check()
        board.draw_board()
        pygame.display.flip()
run_game()