import random

import pygame

import pause_menu
import variables
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
KNIGHT_SIZE_W = 80  # 180
KNIGHT_SIZE_H = 80
KNIGHT_SCALE = 7
KNIGHT_OFFSET = [30, 30]
KNIGHT_DATA = [KNIGHT_SIZE_W, WIZARD_SIZE_H, KNIGHT_SCALE, KNIGHT_OFFSET]

# загрузка фона

# загрузка таблиц
knight_sheet = pygame.image.load("assets/Renegade.png").convert_alpha()  # пояснение в readme
wizard_sheet = pygame.image.load("assets/Vigilante.png").convert_alpha()  # пояснение в readme

# определение количества steps в каждой анимации
KNIGHT_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
WIZARD_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]

fighter_1 = 0
fighter_2 = 0
fighter_3 = 0


def create_fighters():
    global fighter_1, fighter_2, fighter_3
    fighter_1 = Fighter(200, 350, False, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS)
    fighter_2 = Fighter_bot(700, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)
    fighter_3 = Fighter_bot(500, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)


def main_game():
    # создание двух экземпляров бойцов

    # игровой цикл
    run = True
    while run:
        clock.tick(FPS)  # задержка
        # отрисовка фона
        Func.draw_bg(level_game)
        # показать здоровье игрока
        Func.draw_health_bar(fighter_1.health, 20, 20)
        # Func.draw_health_bar(fighter_2.health, 580, 20)

        rand_protection = random.randint(0, 3)  # не защищается, прыжок, сдвиг назад, прыжок со сдвигом

        # передвежение персонажей
        fighter_1.move_for2(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, fighter_3)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)
        fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)

        # update fighters
        fighter_1.update_for2()
        fighter_2.update()
        fighter_3.update()

        # отрисовка персонажей
        fighter_1.draw_for2(screen)
        fighter_2.draw(screen)
        fighter_3.draw(screen)

        # проверка на смерть героя
        if fighter_1.alive == False:
            # game_over_menu.main()
            Func.draw_game_over(level_game)
            return
            # break

        # проверка перехода на след уровень
        if fighter_2.alive == False and fighter_3.alive == False and fighter_1.rect.right > SCREEN_WIDTH:
            LEVEL = 1
            run = False

        # обработчик событий
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu.main()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
