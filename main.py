import configparser

import pygame

import Level1
import Level2
import Level3
import Level4
import main_menu
import video


def main():
    config = configparser.ConfigParser()
    config.read("fighter.ini")
    config.set("fighter", "health", "200")
    config.set("fighter", "level", "3")
    config.set("fighter", "ultra", "3")

    with open("fighter.ini", "w") as config_file:
        config.write(config_file)

    pygame.init()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))

    if Level == 1:
        video.intro_credits()
        video.level_1_credits()
        video.level_1_cut_scene()
        Level1.create_fighters()
        Level1.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))

    if Level == 2:
        video.level_2_credits()
        video.level_2_cut_scene()
        Level2.create_fighters()
        Level2.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))

    if Level == 3:
        video.level_3_credits()
        video.level_3_cut_scene()
        Level3.create_fighters()
        Level3.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))

    if Level == 4:
        video.level_4_credits()
        video.level_4_cut_scene()
        Level4.create_fighters()
        Level4.main_game()

    config.read("fighter.ini")
    Level = int(config.get("fighter", "level"))

    if Level == 5:
        video.level_final_credits()
        video.the_end()
        main_menu.main()

    # выход из pygame
    pygame.quit()
