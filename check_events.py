import sys
import pygame

def exit_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
