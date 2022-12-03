import random

import pygame

from bot_fighter import Fighter_bot
from fighter import Fighter

# уровень
LEVEL = 0

# создаем окно
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

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
bg_image = pygame.image.load("assets/bg.gif").convert_alpha()

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


# функция для прорисовки фона
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# функция для рисования полосы здоровья
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


def main_game():
    # игровой цикл
    run = True
    while run:

        clock.tick(FPS)  # задержка
        # отрисовка фона
        draw_bg()

        # показать здоровье игрока
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

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
