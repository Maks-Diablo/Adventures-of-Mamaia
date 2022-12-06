import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

import Level1
import Level2
import Level3
import variables

FPS = 60


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game():
    if Level1.LEVEL == 0:
        Level1.main_game()
    if Level2.LEVEL == 0:
        Level2.main_game()
    if Level3.LEVEL == 0:
        Level3.main_game()


background_image = pygame_menu.BaseImage(
    image_path="assets/bg.png"
)


def main_background() -> None:
    background_image.draw(surface)


WINDOW_SIZE = (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)


def main(test: bool = False) -> None:
    global clock
    global surface
    theme = pygame_menu.themes.THEME_DEFAULT.copy()
    theme.set_background_color_opacity(0)  # 50% opacity
    menu = pygame_menu.Menu('Welcome', variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT,
                            theme=theme)

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    clock = pygame.time.Clock()

    surface = create_example_window('Example - Game Selector', WINDOW_SIZE)

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
        if menu.is_enabled():
            menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break
