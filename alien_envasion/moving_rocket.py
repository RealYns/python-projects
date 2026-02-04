import sys
import pygame
from settings import Settings
from rocket import Rocket
import game_function_rocket as gfr


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(ai_settings, screen)



    while True:
        gfr.check_events(rocket)
        rocket.update()
        gfr.update_screen(ai_settings, screen, rocket)

run_game()
