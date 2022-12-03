import random

import pygame

import variables
from bot_fighter import Fighter_bot
from fighter import Fighter
from main_functions import Func

# уровень
LEVEL = 0
level_game = 2

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
WIZARD_SIZE = 180  # 150
WIZARD_SCALE = 3
WIZARD_OFFSET = [57, 56]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
KNIGHT_SIZE = 150  # 180
KNIGHT_SCALE = 4
KNIGHT_OFFSET = [57, 56]
KNIGHT_DATA = [KNIGHT_SIZE, KNIGHT_SCALE, KNIGHT_OFFSET]

# загрузка фона

# загрузка таблиц
knight_sheet = [pygame.image.load("assets/Evil Wizard/Sprites/Idle.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Move.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Idle.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Attack.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Attack.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Take Hit.png").convert_alpha(),
                pygame.image.load("assets/Evil Wizard/Sprites/Death.png").convert_alpha()]  # пояснение в readme
wizard_sheet = [pygame.image.load("assets/Hero Knight/Sprites/Idle.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Run.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Jump.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Attack1.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Attack2.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Take Hit.png").convert_alpha(),
                pygame.image.load("assets/Hero Knight/Sprites/Death.png").convert_alpha()]  # пояснение в readme

# определение количества steps в каждой анимации
KNIGHT_ANIMATION_STEPS = [8, 8, 8, 8, 8, 4, 5]
WIZARD_ANIMATION_STEPS = [11, 8, 3, 7, 7, 4, 11]

# создание двух экземпляров бойцов
fighter_1 = Fighter(200, 350, False, KNIGHT_DATA, knight_sheet, KNIGHT_ANIMATION_STEPS)
fighter_2 = Fighter_bot(700, 350, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)


def main_game():
    # игровой цикл
    run = True
    while run:

        clock.tick(FPS)  # задержка
        # отрисовка фона
        Func.draw_bg(level_game)

        # показать здоровье игрока
        Func.draw_health_bar(fighter_1.health, 20, 20)
        Func.draw_health_bar(fighter_2.health, 580, 20)

        rand_protection = random.randint(0, 3)  # не защищается, прыжок, сдвиг назад, прыжок со сдвигом

        # передвежение персонажей
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)

        # update fighters
        fighter_1.update()
        fighter_2.update()

        # отрисовка персонажей
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # проверка перехода на след уровень
        if fighter_2.alive == False and fighter_1.rect.right > SCREEN_WIDTH:
            LEVEL = 1
            run = False

        # обработчик событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
