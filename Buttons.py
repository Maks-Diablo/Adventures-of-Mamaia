import pygame

pygame.init()


class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        pygame.font.init()

        font_size = int(length // len(text))
        myFont = pygame.font.Font("assets/Pixeboy-z8XGD.ttf", font_size)
        myText = myFont.render(text, True, text_color)
        surface.blit(myText, (x, y))
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
