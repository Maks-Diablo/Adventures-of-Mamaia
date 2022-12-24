import configparser
import random

import pygame
from pygame import mixer

import pause_menu
import variables
from bot_fighter import Fighter_bot
from fighter import Fighter
from main_functions import Func

pygame.init()
mixer.init()

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
WIZARD_SCALE = 4
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
mamai_sheet = pygame.image.load("assets/spritesheets/Renegade.png").convert_alpha()  # пояснение в readme
wizard_sheet = pygame.image.load("assets/spritesheets/Zombie.png").convert_alpha()  # пояснение в readme
aleksis_sheet = pygame.image.load("assets/spritesheets/Vigilante.png").convert_alpha()  # пояснение в readme

# определение количества steps в каждой анимации
MAMAI_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
WIZARD_ANIMATION_STEPS = [8, 7, 8, 4, 5, 3]
ALEKSIS_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]


# создание экземпляров бойцов
def create_fighters():
    global fighter_1, fighter_2
    health = 100
    fighter_1 = Fighter(200, 794, False, MAMAI_DATA, mamai_sheet, MAMAI_ANIMATION_STEPS)
    fighter_2 = Fighter_bot(700, 894, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, health)


def main_game():
    # загрузка музыки
    pygame.mixer.music.load("assets/audio/other/philos.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0, 5000)

    mamai_sound_punch = variables.mamai_sound_punch
    mamai_sound_hit = variables.mamai_sound_hit
    bot_sound_punch = variables.bot_sound_punch
    bot_sound_hit = variables.bot_sound_hit

    # игровой цикл
    run = True
    while run:
        clock.tick(FPS)  # задержка

        # отрисовка фона
        Func.draw_bg(level_game)

        # показать здоровье игрока
        Func.draw_health_bar(fighter_1.health, 0, 0)

        # передвежение персонажей
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

        # update fighters
        mamai_punch_sound = pygame.mixer.Sound(random.choice(mamai_sound_punch))
        mamai_punch_sound.set_volume(0.5)
        mamai_hit_sound = pygame.mixer.Sound(random.choice(mamai_sound_hit))
        mamai_hit_sound.set_volume(0.5)

        bot_punch_sound = pygame.mixer.Sound(random.choice(bot_sound_punch))
        bot_punch_sound.set_volume(0.5)
        bot_hit_sound = pygame.mixer.Sound(random.choice(bot_sound_hit))
        bot_hit_sound.set_volume(0.5)

        if fighter_2.attacking and fighter_2.sound_punch:
            bot_punch_sound.play(0)
            fighter_2.sound_punch = False
        if fighter_2.hit and fighter_2.sound_hit:
            bot_hit_sound.play(0)
            fighter_2.sound_hit = False
        if fighter_1.attacking and fighter_1.sound_punch:
            mamai_punch_sound.play(0)
            fighter_1.sound_punch = False
        if fighter_1.hit and fighter_1.sound_hit:
            mamai_hit_sound.play(0)
            fighter_1.sound_hit = False

        fighter_1.update()
        fighter_2.update()

        fighter_2.health = 100

        # отрисовка персонажей
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # проверка на смерть героя
        if fighter_1.alive == False:
            LEVEL = 1
            config = configparser.ConfigParser()
            config.read("fighter.ini")
            config.set("fighter", "health", "200")
            config.set("fighter", "level", "4")
            config.set("fighter", "ultra", str(fighter_1.ultra_aleksis))
            with open("fighter.ini", "w") as config_file:
                config.write(config_file)
            run = False

        # обработчик событий
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu.main()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
