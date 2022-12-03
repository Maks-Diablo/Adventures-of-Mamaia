import pygame

# создаем окно
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
