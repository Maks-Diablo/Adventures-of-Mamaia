import configparser
import random
import time

import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip
from pygame import mixer

import pause_menu
import variables
from bot_aleksis import Aleksis_bot
from bot_fighter import Fighter_bot
from fighter import Fighter
from main_functions import Func

pygame.init()
mixer.init()

# уровень
LEVEL = 0
level_game = 1

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
wizard_sheet = pygame.image.load("assets/Ranger.png").convert_alpha()  # пояснение в readme
aleksis_sheet = pygame.image.load("assets/Vigilante.png").convert_alpha()  # пояснение в readme

# определение количества steps в каждой анимации
MAMAI_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
WIZARD_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
ALEKSIS_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]


# создание экземпляров бойцов
def create_fighters():
    global fighter_1, fighter_2, fighter_3
    fighter_1 = Fighter(200, 794, False, MAMAI_DATA, mamai_sheet, MAMAI_ANIMATION_STEPS)
    fighter_2 = Fighter_bot(700, 794, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)
    fighter_3 = Aleksis_bot(-10, 794, False, ALEKSIS_DATA, aleksis_sheet, ALEKSIS_ANIMATION_STEPS)
    fighter_3.attack_run = True
    variables.video_bool = True


def main_game():
    # загрузка музыки
    pygame.mixer.music.load("assets/audio/other/club.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0, 5000)

    mamai_sound_punch = variables.mamai_sound_punch
    mamai_sound_hit = variables.mamai_sound_hit
    bot_sound_punch = variables.bot_sound_punch
    bot_sound_hit = variables.bot_sound_hit
    aleksis_sound = variables.aleksis_sound

    aleksis_sound_bool = True
    aleksis = False
    timing_ultra = time.time()
    # игровой цикл
    run = True
    while run:
        clock.tick(FPS)  # задержка
        # отрисовка фона
        Func.draw_bg(level_game)
        # показать здоровье игрока
        Func.draw_health_bar(fighter_1.health, 0, 0)

        # показать уровень ульты игрока
        Func.draw_ultra_bar(fighter_1.ultra_aleksis, 0, 0)

        # таймер ульты
        if time.time() - timing_ultra > 5.0 and fighter_1.ultra_aleksis != 3:
            timing_ultra = time.time()
            fighter_1.ultra_aleksis += 1

        rand_protection = random.randint(0, 3)  # не защищается, прыжок, сдвиг назад, прыжок со сдвигом

        # передвежение персонажей
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, rand_protection)
        if aleksis == True:
            fighter_3.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, rand_protection)

        # update fighters
        mamai_punch_sound = pygame.mixer.Sound(random.choice(mamai_sound_punch))
        mamai_punch_sound.set_volume(0.5)
        mamai_hit_sound = pygame.mixer.Sound(random.choice(mamai_sound_hit))
        mamai_hit_sound.set_volume(0.5)

        bot_punch_sound = pygame.mixer.Sound(random.choice(bot_sound_punch))
        bot_punch_sound.set_volume(0.5)
        bot_hit_sound = pygame.mixer.Sound(random.choice(bot_sound_hit))
        bot_hit_sound.set_volume(0.5)

        sound_aleksis = pygame.mixer.Sound(random.choice(aleksis_sound))
        sound_aleksis.set_volume(1)

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
        if fighter_3.attacking and fighter_3.sound_punch:
            fighter_3.sound_punch = False

        fighter_1.update()
        fighter_2.update()
        if aleksis == True:
            if aleksis_sound_bool:
                sound_aleksis.play(0)
                aleksis_sound_bool = False
            fighter_3.update()

        # отрисовка персонажей
        fighter_1.draw(screen)
        fighter_2.draw(screen)
        if aleksis == True:
            fighter_3.draw(screen)

        # проверка на смерть героя
        if fighter_1.alive == False:
            # game_over_menu.main()
            Func.draw_game_over(level_game)
            main_game()

        if fighter_3.attack_run and fighter_3.rect.right < 0:
            aleksis = False

        # проверка перехода на след уровень
        if fighter_2.alive == False and variables.video_bool:
            if time.time() - timing_ultra > 5.0:
                timing_ultra = time.time()
                clip = VideoFileClip('assets/video/cast-scene-level1_2(0).mp4')
                clipresized = clip.resize(height=variables.SCREEN_HEIGHT)
                clipresized.preview()
                variables.video_bool = False

        if fighter_2.alive == False and fighter_1.rect.right > SCREEN_WIDTH:
            LEVEL = 1
            config = configparser.ConfigParser()
            config.read("fighter.ini")
            config.set("fighter", "health", str(fighter_1.health))
            config.set("fighter", "level", "2")
            config.set("fighter", "ultra", str(fighter_1.ultra_aleksis))
            with open("fighter.ini", "w") as config_file:
                config.write(config_file)
            run = False

        # обработчик событий
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu.main()
            break

        for event in pygame.event.get():
            # создание алексиса
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and fighter_1.ultra_aleksis != 0:
                aleksis = True
                fighter_3.rect.x = -10
                fighter_3.attack_run = False
                aleksis_sound_bool = True

                config = configparser.ConfigParser()

                if fighter_1.ultra_aleksis == 2:
                    fighter_1.ultra_aleksis = 1
                    fighter_3.ultra_attack = 1

                elif fighter_1.ultra_aleksis == 1:
                    fighter_1.ultra_aleksis = 0
                    fighter_3.ultra_attack = 1

                elif fighter_1.ultra_aleksis == 3:
                    fighter_1.ultra_aleksis = 0
                    fighter_3.ultra_attack = 2

                # запись изменения ульты
                config2 = configparser.ConfigParser()
                config2.read("fighter.ini")
                if int(config2.get("fighter", "ultra")) != fighter_1.ultra_aleksis:
                    config2.set("fighter", "ultra", str(fighter_1.ultra_aleksis))
                    with open("fighter.ini", "w") as config_file:
                        config2.write(config_file)

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
