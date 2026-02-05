import pygame
from pygame.sprite import Group
from settings1 import Settings1
from ship1 import Ship1
import game_function_ship1 as gfs1


def run_game():
    pygame.init()
    ai_settings = Settings1()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("sideways shooter test")
    ship1 = Ship1(ai_settings, screen)
    bullets = Group()



    while True:
        gfs1.check_events(ai_settings, screen, ship1, bullets)
        ship1.update()
        gfs1.update_bullets(ai_settings, bullets)
        gfs1.update_screen(ai_settings, screen, ship1, bullets)

run_game()
