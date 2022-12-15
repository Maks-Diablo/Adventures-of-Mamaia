import time
timing = time.time()
while True:
    if time.time() - timing > 10.0:
        timing = time.time()
        print("10 seconds")

# """
# pygame-menu
# https://github.com/ppizarror/pygame-menu
# EXAMPLE - IMAGE BACKGROUND
# Menu using background image + BaseImage object.
# """
#
# __all__ = ['main']
#
# import pygame
# import pygame_menu
# from pygame_menu.examples import create_example_window
# import variables
# from typing import Optional
#
# # Constants and global variables
# FPS = 60
# WINDOW_SIZE = (variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT)
#
#
#
# # Load image
# background_image = pygame_menu.BaseImage(
#     image_path="assets/bg.png"
# )
#
#
# def main_background() -> None:
#     background_image.draw(surface)
#
#
# def main(test: bool = False) -> None:
#     global main_menu
#     global sound
#     global surface
#
#     # Create window
#     surface = create_example_window('Example - Image Background', WINDOW_SIZE)
#     clock = pygame.time.Clock()
#
#     # Create menus: Main menu
#     main_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
#     main_menu_theme.set_background_color_opacity(0.5)  # 50% opacity
#
#     main_menu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.7,
#         onclose=pygame_menu.events.EXIT,  # User press ESC button
#         theme=main_menu_theme,
#         title='Epic Menu',
#         width=WINDOW_SIZE[0] * 0.8
#     )
#
#     theme_bg_image = main_menu_theme.copy()
#
#     theme_bg_image.title_font_size = 25
#
#
#
#
#
#     button_image = pygame_menu.BaseImage(pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)
#
#
#     main_menu.add.button('Another fancy button', lambda: print('This button has been pressed'))
#     main_menu.add.button('Quit', pygame_menu.events.EXIT)
#
#     # Main loop
#     while True:
#
#         # Tick
#         clock.tick(FPS)
#
#         # Main menu
#         main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)
#
#         # Flip surface
#         pygame.display.flip()
#
#         # At first loop returns
#         if test:
#             break
#
#
# if __name__ == '__main__':
#     main()