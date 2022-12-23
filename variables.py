import pygame

# создаем окно
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# звуковые эффекты
mamai_sound_punch = ["assets/audio/punch1.mp3", "assets/audio/punch2.mp3",
                         "assets/audio/punch3.mp3", "assets/audio/punch4.mp3", "assets/audio/punch5.mp3",
                         "assets/audio/punch6.mp3", "assets/audio/punch7.mp3"]
mamai_sound_hit = ["assets/audio/hit3_1.mp3", "assets/audio/hit3_2.mp3", "assets/audio/hit3_3.mp3",
                   "assets/audio/hit3_4.mp3", "assets/audio/hit3_5.mp3", "assets/audio/hit3_6.mp3",
                   "assets/audio/hit3_7.mp3", "assets/audio/hit3_8.mp3", "assets/audio/hit3_9.mp3",
                   "assets/audio/hit3_10.mp3", "assets/audio/hit3_11.mp3", "assets/audio/hit3_12.mp3",
                   "assets/audio/hit3_13.mp3", "assets/audio/hit3_14.mp3", "assets/audio/hit3_15.mp3",
                   "assets/audio/hit3_16.mp3"]
bot_sound_punch = ["assets/audio/punch8.mp3", "assets/audio/punch9.mp3", "assets/audio/punch10.mp3",
                     "assets/audio/punch11.mp3", "assets/audio/punch12.mp3", "assets/audio/punch13.mp3",
                     "assets/audio/punch14.mp3", "assets/audio/punch15.mp3"]
bot_sound_hit = ["assets/audio/hit2_1.mp3", "assets/audio/hit2_2.mp3", "assets/audio/hit2_3.mp3",
                   "assets/audio/hit2_4.mp3", "assets/audio/hit2_5.mp3", "assets/audio/hit2_6.mp3",
                   "assets/audio/hit2_7.mp3", "assets/audio/hit2_8.mp3", "assets/audio/hit2_9.mp3",
                   "assets/audio/hit2_10.mp3"]
aleksis_sound = ["assets/audio/aleksis/audio1.mp3", "assets/audio/aleksis/audio2.mp3", "assets/audio/aleksis/audio3.mp3"]

video_bool = False