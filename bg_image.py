import pygame


def bg_image(bg):
    if bg == 1:
        bg_image = pygame.image.load("assets/backgrounds/City2.jpg").convert_alpha()
    if bg == 2:
        bg_image = pygame.image.load("assets/backgrounds/War2.png").convert_alpha()
    if bg == 3:
        bg_image = pygame.image.load("assets/backgrounds/school.png").convert_alpha()
    if bg == 4:
        bg_image = pygame.image.load("assets/backgrounds/postapocalypse3.png").convert_alpha()
    return bg_image
