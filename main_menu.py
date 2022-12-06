__all__ = ['main']

from random import randrange
from typing import Tuple, Any, Optional, List

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

import main as main_loop
import variables

# Constants and global variables
ABOUT = [f'Game {"v11"}',
         f'Author: {"Diablo"}',
         f'Email: {"@weregrht"}']
DIFFICULTY = ['EASY']
FPS = 60
WINDOW_SIZE = (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)

clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None


def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty


def random_color() -> Tuple[int, int, int]:
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty: List, font: 'pygame.font.Font', test: bool = False) -> None:
    main_loop.main()


background_image = pygame_menu.BaseImage(
    image_path="assets/bg.png"
)


def main_background() -> None:
    background_image.draw(surface)


def main(test: bool = False) -> None:
    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window('Example - Game Selector', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    play_menu_theme.set_background_color_opacity(0)  # 50% opacity
    play_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=play_menu_theme,
        title='Play Menu',
        width=WINDOW_SIZE[0]
    )

    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.set_background_color_opacity(0)  # 50% opacity
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=submenu_theme,
        title='Submenu',
        width=WINDOW_SIZE[0]
    )

    play_submenu.add.button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))
    play_menu.add.selector('Select difficulty ',
                           [('1 - Easy', 'EASY'),
                            ('2 - Medium', 'MEDIUM'),
                            ('3 - Hard', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
    play_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    about_theme.set_background_color_opacity(0)  # 50% opacity

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0]
    )

    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    # about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    main_theme.set_background_color_opacity(0)  # 50% opacity

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0]
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
