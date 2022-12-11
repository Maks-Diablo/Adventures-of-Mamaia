import configparser

import pygame

import Level1
import Level2
import Level3


def main():
    config = configparser.ConfigParser()
    config.read("fighter.ini")
    config.set("fighter", "health", "200")
    config.set("fighter", "level", "1")
    with open("fighter.ini", "w") as config_file:
        config.write(config_file)

    pygame.init()

    Level = int(config.get("fighter", "level"))

    if Level == 1:
        Level1.create_fighters()
        Level1.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))
    if Level == 2:
        Level2.create_fighters()
        Level2.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))
    if Level == 3:
        Level3.create_fighters()
        Level3.main_game()
    # выход из pygame
    pygame.quit()
