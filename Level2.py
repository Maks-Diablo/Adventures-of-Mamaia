import configparser
import random
import time

import pygame
from pygame import mixer

import pause_menu
import variables
from bot_aleksis import Aleksis_bot
from bot_fighter import Fighter_bot
from fighter import Fighter
from main_functions import Func

mixer.init()
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
BOT_SIZE_W = 80  # 150
BOT_SIZE_H = 80
BOT_SCALE = 7
BOT_OFFSET = [30, 30]
BOT_DATA = [BOT_SIZE_W, BOT_SIZE_H, BOT_SCALE, BOT_OFFSET]
SOLDIER_SIZE_W = 80  # 150
SOLDIER_SIZE_H = 80
SOLDIER_SCALE = 7
SOLDIER_OFFSET = [30, 30]
SOLDIER_DATA = [SOLDIER_SIZE_W, SOLDIER_SIZE_H, SOLDIER_SCALE, SOLDIER_OFFSET]
MAMAI_SIZE_W = 80  # 180
MAMAI_SIZE_H = 80
MAMAI_SCALE = 7
MAMAI_OFFSET = [30, 30]
MAMAI_DATA = [MAMAI_SIZE_W, SOLDIER_SIZE_H, MAMAI_SCALE, MAMAI_OFFSET]
ALEKSIS_SIZE_W = 80  # 180
ALEKSIS_SIZE_H = 80
ALEKSIS_SCALE = 7
ALEKSIS_OFFSET = [30, 30]
ALEKSIS_DATA = [ALEKSIS_SIZE_W, SOLDIER_SIZE_H, ALEKSIS_SCALE, ALEKSIS_OFFSET]

# загрузка таблиц
mamai_sheet = pygame.image.load("assets/spritesheets/Renegade.png").convert_alpha()  # пояснение в readme
soldier_sheet = pygame.image.load("assets/spritesheets/Soldier2.png").convert_alpha()  # пояснение в readme
bot_sheet = pygame.image.load("assets/spritesheets/Soldier2_bot.png").convert_alpha()  # пояснение в readme
aleksis_sheet = pygame.image.load("assets/spritesheets/Vigilante.png").convert_alpha()  # пояснение в readme

# определение количества steps в каждой анимации
MAMAI_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
SOLDIER_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
BOT_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]
ALEKSIS_ANIMATION_STEPS = [4, 4, 4, 1, 1, 1, 1]


def create_fighters():
    global fighter_mamai, fighter_soldier_bot, fighter_aleksis, fighter_bot1, fighter_bot2
    health = Func.change_difficulty(0)

    fighter_mamai = Fighter(200, 794, False, MAMAI_DATA, mamai_sheet, MAMAI_ANIMATION_STEPS)
    fighter_soldier_bot = Fighter_bot(700, 794, True, SOLDIER_DATA, soldier_sheet, SOLDIER_ANIMATION_STEPS, health)
    fighter_bot1 = Fighter_bot(500, 794, True, BOT_DATA, bot_sheet, BOT_ANIMATION_STEPS, health)
    fighter_bot2 = Fighter_bot(600, 794, True, BOT_DATA, bot_sheet, BOT_ANIMATION_STEPS, health)
    fighter_aleksis = Aleksis_bot(-10, 794, False, ALEKSIS_DATA, aleksis_sheet, ALEKSIS_ANIMATION_STEPS)
    fighter_aleksis.attack_run = True


def main_game():
    # загрузка музыки
    pygame.mixer.music.load("assets/audio/other/war.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1, 0.0, 5000)

    mamai_sound_punch = variables.mamai_sound_punch
    mamai_sound_hit = variables.mamai_sound_hit
    bot_sound_punch = variables.bot_sound_punch
    bot_sound_hit = variables.bot_sound_hit
    aleksis_sound = variables.aleksis_sound

    aleksis_sound_bool = True

    aleksis = False
    bot1 = 0
    bot2 = 0

    timing_ultra = time.time()

    # игровой цикл
    run = True
    while run:
        clock.tick(FPS)  # задержка

        # отрисовка фона
        Func.draw_bg(level_game)

        # показать здоровье игрока
        Func.draw_health_bar(fighter_mamai.health, 0, 0)

        # показать уровень ульты игрока
        Func.draw_ultra_bar(fighter_mamai.ultra_aleksis, 0, 0)

        # таймер ульты
        if time.time() - timing_ultra > 5.0 and fighter_mamai.ultra_aleksis != 3:
            timing_ultra = time.time()
            fighter_mamai.ultra_aleksis += 1

        # таймер перерождения ботов
        if time.time() - timing_ultra > 2.0 and (fighter_bot1.alive == False or fighter_bot2.alive == False) and (
                bot1 == 0 or bot2 == 0):
            timing_ultra = time.time()
            if fighter_bot1.alive == False: bot1 = 1
            if fighter_bot2.alive == False: bot2 = 1

        rand_protection = random.randint(0, 3)  # не защищается, прыжок, сдвиг назад, прыжок со сдвигом

        # передвежение персонажей
        fighter_mamai.move_for3(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_soldier_bot, fighter_bot1, fighter_bot2)
        fighter_soldier_bot.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_mamai)

        if aleksis == True:
            fighters_list_alive = [fighter_soldier_bot, fighter_bot1, fighter_bot2]
            if fighter_soldier_bot in fighters_list_alive and fighter_soldier_bot.alive == False:
                fighters_list_alive.remove(fighter_soldier_bot)
            if fighter_bot1 in fighters_list_alive and fighter_bot1.alive == False:
                fighters_list_alive.remove(fighter_bot1)
            if fighter_bot2 in fighters_list_alive and fighter_bot2.alive == False:
                fighters_list_alive.remove(fighter_bot2)

            if fighter_soldier_bot not in fighters_list_alive and fighter_soldier_bot.alive == True:
                fighters_list_alive.append(fighter_soldier_bot)
            if fighter_bot1 not in fighters_list_alive and fighter_bot1.alive == True:
                fighters_list_alive.append(fighter_bot1)
            if fighter_bot2 not in fighters_list_alive and fighter_bot2.alive == True:
                fighters_list_alive.append(fighter_bot2)

            try:
                target = random.choice(fighters_list_alive)
            except:
                target = fighter_soldier_bot

            fighter_aleksis.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, target, 2)

        fighter_bot1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_mamai)
        fighter_bot2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_mamai)

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

        if fighter_soldier_bot.attacking and fighter_soldier_bot.sound_punch:
            bot_punch_sound.play(0)
            fighter_soldier_bot.sound_punch = False
        if fighter_soldier_bot.hit and fighter_soldier_bot.sound_hit:
            bot_hit_sound.play(0)
            fighter_soldier_bot.sound_hit = False
        if fighter_bot1.attacking and fighter_bot1.sound_punch:
            bot_punch_sound.play(0)
            fighter_bot1.sound_punch = False
        if fighter_bot1.hit and fighter_bot1.sound_hit:
            bot_hit_sound.play(0)
            fighter_bot1.sound_hit = False
        if fighter_bot2.attacking and fighter_bot2.sound_punch:
            bot_punch_sound.play(0)
            fighter_bot2.sound_punch = False
        if fighter_bot2.hit and fighter_bot2.sound_hit:
            bot_hit_sound.play(0)
            fighter_bot2.sound_hit = False
        if fighter_mamai.attacking and fighter_mamai.sound_punch:
            mamai_punch_sound.play(0)
            fighter_mamai.sound_punch = False
        if fighter_mamai.hit and fighter_mamai.sound_hit:
            mamai_hit_sound.play(0)
            fighter_mamai.sound_hit = False

        fighter_mamai.update()
        fighter_soldier_bot.update()
        if aleksis == True:
            if aleksis_sound_bool:
                sound_aleksis.play(0)
                aleksis_sound_bool = False
            fighter_aleksis.update()
        fighter_bot1.update()
        fighter_bot2.update()

        # отрисовка персонажей
        fighter_mamai.draw(screen)
        fighter_soldier_bot.draw(screen)
        if aleksis == True:
            fighter_aleksis.draw(screen)
        fighter_bot1.draw(screen)
        fighter_bot2.draw(screen)

        # проверка на смерть бота 1
        if fighter_bot1.alive == False and bot1 == 1:
            bot1 = 2
            fighter_bot1.alive = True
            fighter_bot1.health = 10
            fighter_bot1.rect.right = -10

        # проверка на смерть бота 2
        if fighter_bot2.alive == False and bot2 == 1:
            bot2 = 2
            fighter_bot2.alive = True
            fighter_bot2.health = 10
            fighter_bot2.rect.left = 1930

        # проверка на смерть героя
        if fighter_mamai.alive == False:
            Func.draw_game_over(level_game)

        if fighter_aleksis.attack_run and fighter_aleksis.rect.right < 0:
            aleksis = False

        # проверка перехода на след уровень
        if fighter_bot1.alive == False and fighter_bot2.alive == False and fighter_soldier_bot.alive == False and fighter_mamai.rect.right > SCREEN_WIDTH:
            LEVEL = 1
            config = configparser.ConfigParser()
            config.read("fighter.ini")
            config.set("fighter", "health", str(fighter_mamai.health))
            config.set("fighter", "level", "3")
            config.set("fighter", "ultra", str(fighter_mamai.ultra_aleksis))
            with open("fighter.ini", "w") as config_file:
                config.write(config_file)
            run = False

        # обработчик событий
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pause_menu.main()

        for event in pygame.event.get():
            # создание алексиса
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z and fighter_mamai.ultra_aleksis != 0:
                aleksis = True
                fighter_aleksis.rect.x = -10
                fighter_aleksis.attack_run = False
                aleksis_sound_bool = True

                config = configparser.ConfigParser()

                if fighter_mamai.ultra_aleksis == 2:
                    fighter_mamai.ultra_aleksis = 1
                    fighter_aleksis.ultra_attack = 1

                elif fighter_mamai.ultra_aleksis == 1:
                    fighter_mamai.ultra_aleksis = 0
                    fighter_aleksis.ultra_attack = 1

                elif fighter_mamai.ultra_aleksis == 3:
                    fighter_mamai.ultra_aleksis = 0
                    fighter_aleksis.ultra_attack = 2

                # запись изменения ульты
                config2 = configparser.ConfigParser()
                config2.read("fighter.ini")
                if int(config2.get("fighter", "ultra")) != fighter_mamai.ultra_aleksis:
                    config2.set("fighter", "ultra", str(fighter_mamai.ultra_aleksis))
                    with open("fighter.ini", "w") as config_file:
                        config2.write(config_file)

            if event.type == pygame.QUIT:
                run = False
                LEVEL = 1

        pygame.display.update()
