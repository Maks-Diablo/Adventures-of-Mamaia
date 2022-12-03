import pygame

import bg_image
import variables

screen = variables.screen
SCREEN_WIDTH = variables.SCREEN_WIDTH
SCREEN_HEIGHT = variables.SCREEN_HEIGHT
clock = variables.clock
FPS = variables.FPS
# define colours
YELLOW = variables.YELLOW
RED = variables.RED
WHITE = variables.WHITE


class Func:
    # функция для прорисовки фона
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(bg_image.bg_image(self), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

    # функция для рисования полосы здоровья
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
