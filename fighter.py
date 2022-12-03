import pygame


class Fighter():
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 184, 150))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.hit = False
        self.health = 1000
        self.alive = True
        self.health_damage = 10

        # проверка уровня
        self.level = 0  # 0 - игра, 1 - пройден

    def load_images(self, sprite_sheet, animation_steps):
        # извлечение изображения из листа спрайтов
        animation_list = []
        for i in range(len(sprite_sheet)):
            animation_steps2 = [animation_steps[i]]
            for y, animation in enumerate(animation_steps2):
                temp_img_list = []
                for x in range(animation):
                    temp_image = sprite_sheet[i].subsurface(x * self.size, y * self.size, self.size, self.size)
                    temp_img_list.append(
                        pygame.transform.scale(temp_image,
                                               (self.size * self.image_scale, self.size * self.image_scale)))
                animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        # get keypresses
        key = pygame.key.get_pressed()

        # может выполнять действия только если не атакует
        if self.attacking == False and self.alive == True:
            # movement
            if key[pygame.K_a]:
                dx = -SPEED
                self.running = True
                if target.alive == False:
                    self.flip = True
            if key[pygame.K_d]:
                dx = SPEED
                self.running = True
                if target.alive == False:
                    self.flip = False

            # прыжок
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            # атака
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)
                # опредление вида атаки
                if key[pygame.K_r]:
                    self.attack_type = 1
                    self.health_damage = 10
                if key[pygame.K_t]:
                    self.attack_type = 2
                    self.health_damage = 20

        # добавление гравитации
        self.vel_y += GRAVITY
        dy += self.vel_y

        # проверка уровня
        if target.level == 1: self.level = 1

        # остановка персонажа на краях
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width and self.level == 0 and target.alive == True:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 70:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 70 - self.rect.bottom

        # убеждаемся, что персонажи смотрят друг на друга
        if self.alive == True and target.alive == True:
            if target.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True

        # apply attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # обновляем позицию игрока
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        # проверка какая анимация
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(6)  # Death
        elif self.hit == True:
            self.update_action(5)
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)  # Attack1
            elif self.attack_type == 2:
                self.update_action(4)  # Attack2
        elif self.jump == True:
            self.update_action(2)  # Jump
        elif self.running == True:
            self.update_action(1)  # Run
        else:
            self.update_action(0)  # Idle

        animation_cooldown = 50
        # update image
        self.image = self.animation_list[self.action][self.frame_index]
        # проверка прошло ли достаточно времени с момента последнего обновления
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # проврека закончилась ли анимация
        if self.frame_index >= len(self.animation_list[self.action]):
            # если герой умер последний кадр анимации смерти
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                # была ли атака выполнена
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                    if self.action == 4:
                        self.attack_cooldown = 40
                    elif self.action == 3:
                        self.attack_cooldown = 20  # если была нанесена атака
                if self.action == 5:
                    self.hit = False
                    # если боец находился в середине атаки тогда атака остановлена
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y,
                                         2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= self.health_damage
                target.hit = True
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            # обновить настройки анимации
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (
            self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
