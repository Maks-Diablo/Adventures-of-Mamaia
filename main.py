import pygame

import Level1
import Level2
import Level3



def main():
    pygame.init()
    Level = 1

    if Level1.LEVEL == 0 and Level == 1:
        Level += 1
        Level1.main_game()
    if Level2.LEVEL == 0 and Level == 2:
        Level += 1
        Level2.main_game()
    if Level3.LEVEL == 0 and Level == 3:
        Level += 1
        Level3.main_game()
    # выход из pygame
    pygame.quit()
