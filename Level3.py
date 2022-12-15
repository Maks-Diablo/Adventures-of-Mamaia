import configparser
import random
import time

import pygame

import pause_menu
import variables
from bot_aleksis import Aleksis_bot
from bot_fighter import Fighter_bot
from fighter import Fighter
from main_functions import Func

# уровень
LEVEL = 0
level_game = 3

screen = variables.screen
SCREEN_WIDTH = variables.SCREEN_WIDTH
SCREEN_HEIGHT = variables.SCREEN_HEIGHT
clock = variables.clock
FPS = variables.FPS

# define colours
YELLOW = variables.YELLOW
RED = variables.RED
WHITE = variables.WHITE

# define fighters variables
WIZARD_SIZE_W = 80  # 150
WIZARD_SIZE_H = 80
WIZARD_SCALE = 7
WIZARD_OFFSET = [30, 30]
WIZARD_DATA = [WIZARD_SIZE_W, WIZARD_SIZE_H, WIZARD_SCALE, WIZARD_OFFSET]
MAMAI_SIZE_W = 80  # 180
MAMAI_SIZE_H = 80
MAMAI_SCALE = 7
MAMAI_OFFSET = [30, 30]
MAMAI_DATA = [MAMAI_SIZE_W, WIZARD_SIZE_H, MAMAI_SCALE, MAMAI_OFFSET]
ALEKSIS_SIZE_W = 80  # 180
ALEKSIS_SIZE_H = 80
ALEKSIS_SCALE = 7
ALEKSIS_OFFSET = [30, 30]
ALEKSIS_DATA = [ALEKSIS_SIZE_W, WIZARD_SIZE_H, ALEKSIS_SCALE, ALEKSIS_OFFSET]
# загрузка фона

# загрузка таблиц
mamai_sheet = pygame.image.load("assets/Renegade.png").convert_alpha()  # пояснение в readme
wizard_sheet = pygame.image.load("assets/Vigilante.png").convert_alpha()  # пояснение в readme
aleksis_sheet = pygame.image.load("assets/Vigilante.png").convert_alpha()  # пояснение в readme

# определение количества steps в каждой анимации
MAMAI_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
WIZARD_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
ALEKSIS_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]




def create_fighters():
    global fighter_1, fighter_2, fighter_3, fighter_4
    fighter_1 = Fighter(200, 794, False, MAMAI_DATA, mamai_sheet, MAMAI_ANIMATION_STEPS)
    fighter_2 = Fighter_bot(700, 794, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)
    fighter_4 = Fighter_bot(500, 794, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)
    fighter_3 = Aleksis_bot(-10, 794, False, ALEKSIS_DATA, aleksis_sheet, ALEKSIS_ANIMATION_STEPS)
    fighter_3.attack_run = True

def main_game():
    aleksis = False
    timing_ultra = time.time()

    # игровой цикл
    run = True
    while run:
        clock.tick(FPS)  # задержка
        # отрисовка фона
        Func.draw_bg(level_game)
        # показать здоровье игрока
        Func.draw_health_bar(fighter_1.health, 20, 20)
        # Func.draw_health_bar(fighter_2.health, 580, 20)

        # показать уровень ульты игрока
        Func.draw_ultra_bar(fighter_1.ultra_aleksis, 0, 0)

        # таймер ульты
        if time.time() - timing_ultra > 5.0 and fighter_1.ultra_aleksis != 3:
            timing_ultra = time.time()
            fighter_1.ultra_aleksis += 1

        rand_protection = random.randint(0, 3)  # не защищается, прыжок, сдвиг назад, прыжок со сдвигом

        # передвежение персонажей
        fighter_1.move_for2(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, fighter_3)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)
        fighter_4.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)
        if aleksis == True:
            fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, rand_protection)

        # update fighters
        fighter_1.update_for2()
        fighter_2.update()
        fighter_4.update()
        if aleksis == True:
            fighter_3.update()

        # отрисовка персонажей
        fighter_1.draw_for2(screen)
        fighter_2.draw(screen)
        fighter_4.draw(screen)
        if aleksis == True:
            fighter_3.draw(screen)

        # проверка на смерть героя
        if fighter_1.alive == False:
            # game_over_menu.main()
            Func.draw_game_over(level_game)

        if fighter_3.attack_run and fighter_3.rect.right < 0:
            aleksis = False

        # проверка перехода на след уровень
        if fighter_2.alive == False and fighter_3.alive == False and fighter_1.rect.right > SCREEN_WIDTH:
            LEVEL = 1
            run = False

        # обработчик событий
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu.main()

        for event in pygame.event.get():
            # создание алексиса
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and fighter_1.ultra_aleksis != 0:
                aleksis = True
                fighter_3.rect.x = -10
                fighter_3.attack_run = False

                if fighter_1.ultra_aleksis == 2:
                    fighter_1.ultra_aleksis = 1
                elif fighter_1.ultra_aleksis == 1:
                    fighter_1.ultra_aleksis = 0
                elif fighter_1.ultra_aleksis == 3:
                    fighter_1.ultra_aleksis = 0
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
