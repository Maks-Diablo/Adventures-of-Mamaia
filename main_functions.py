import configparser

import pygame
from pygame.locals import *

import Buttons
import bg_image
import main_menu
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
    def draw_game_over(self):
        game_over_image = pygame.image.load("assets/game_over.png").convert_alpha()
        scaled_bg = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

        Button1 = Buttons.Button()
        Button2 = Buttons.Button()

        while True:
            Button1.create_button(screen, (107, 142, 35), SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 100, 600, 40, 0,
                                  "Play Again", (255, 255, 255))
            Button2.create_button(screen, (107, 142, 35), SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 150, 230, 40, 0,
                                  "Quit", (255, 255, 255))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if Button1.pressed(pygame.mouse.get_pos()):
                        config = configparser.ConfigParser()
                        config.read("fighter.ini")
                        config.set("fighter", "health", "200")
                        config.set("fighter", "level", "1")
                        with open("fighter.ini", "w") as config_file:
                            config.write(config_file)

                        main_menu.main()
                        return
                    if Button2.pressed(pygame.mouse.get_pos()):
                        pygame.quit()
                        return

    # функция для прорисовки фона
    def draw_bg(self):
        scaled_bg = pygame.transform.scale(bg_image.bg_image(self), (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))

    # функция для рисования полосы здоровья
    def draw_health_bar(health, x, y):
        ratio = health / 10

        for i in range(int(ratio)):
            health_bar_1 = pygame.image.load("assets/Health_1.png").convert_alpha()  # пояснение в readme
            health_scale = pygame.transform.scale(health_bar_1,
                                                  (health_bar_1.get_width() * 3, health_bar_1.get_height() * 3))
            if i >= 10:
                screen.blit(health_scale, (health_bar_1.get_width() * 2 * (i % 10) + 15, health_bar_1.get_height() * 3))
            else:
                screen.blit(health_scale, (health_bar_1.get_width() * 2 * i + 15, health_bar_1.get_height()))

        # pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        # pygame.draw.rect(screen, RED, (x, y, 400, 30))
        # pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
