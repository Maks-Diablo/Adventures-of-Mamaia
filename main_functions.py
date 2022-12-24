import configparser
import math
import time

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
grenade = pygame.transform.scale(pygame.image.load(r"assets/grenade.png"), (50, 50))
x = 0
y = 0
v = 0
vx = 0
vy = 0


class Func:
    def draw_game_over(self):
        game_over_image = pygame.image.load("assets/backgrounds/game_over.png").convert_alpha()
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
                screen.blit(health_scale,
                            (health_bar_1.get_width() * 2 * (i % 10) + 15 + x, health_bar_1.get_height() * 3))
            else:
                screen.blit(health_scale, (health_bar_1.get_width() * 2 * i + 15 + x, health_bar_1.get_height()))

    # функция для рисования полосы ульты
    def draw_ultra_bar(ultra, x, y):
        for i in range(3):
            ultra_bar_1 = pygame.image.load("assets/beer_1.png").convert_alpha()  # пояснение в readme
            ultra_scale1 = pygame.transform.scale(ultra_bar_1,
                                                  (ultra_bar_1.get_width() * 2.5, ultra_bar_1.get_height() * 2.5))
            ultra_bar_0 = pygame.image.load("assets/beer_0.png").convert_alpha()  # пояснение в readme
            ultra_scale0 = pygame.transform.scale(ultra_bar_0,
                                                  (ultra_bar_0.get_width() * 2.5, ultra_bar_0.get_height() * 2.5))
            if i < ultra:
                screen.blit(ultra_scale1,
                            (ultra_bar_1.get_width() * 1.5 * (i % 10) + x, ultra_bar_1.get_height() * 3))
            else:
                screen.blit(ultra_scale0,
                            (ultra_bar_0.get_width() * 1.5 * (i % 10) + x, ultra_bar_0.get_height() * 3))

    @staticmethod
    def change_difficulty(type):
        config = configparser.ConfigParser()
        config.read("fighter.ini")
        difficulty = config.get("fighter", "difficulty")
        if type == 0:
            if int(difficulty) == 0:
                health = 70
            if int(difficulty) == 2:
                health = 10
            if int(difficulty) == 1:
                health = 150
        elif type == 1:
            if int(difficulty) == 0:
                health = 400
            if int(difficulty) == 2:
                health = 300
            if int(difficulty) == 1:
                health = 500
        return health

    @staticmethod
    def draw_grenade(s, t):
        global grenade, x, y, v, vx, vy
        # v = -120
        flag = False
        if x == 0 and y == 0:
            x = SCREEN_WIDTH
            y = 700
            v = -math.sqrt((SCREEN_WIDTH + 300 - s) * 10)
            print()
            # a = math.asin((SCREEN_WIDTH+300-s)*10/(v*v))/2
            vx = v * math.cos(45)
            vy = v * math.sin(45)

        t = (time.time() - t) * 10

        x = SCREEN_WIDTH + 300 + vx * t
        y = 794 + (vy * t + 5 * t * t)
        print(y)
        if x <= s:
            x = s
        if y >= 800:
            y = 800

        if x <= s and y >= 800:
            flag = True

        screen.blit(grenade, (x, y))
        return flag
