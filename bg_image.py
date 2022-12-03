import pygame


def bg_image(bg):
    if bg == 1:
        bg_image = pygame.image.load("assets/bg.gif").convert_alpha()
    if bg == 2:
        bg_image = pygame.image.load("assets/Level2/background.png").convert_alpha()
    return bg_image
