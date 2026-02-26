import pygame
from character import Character
from ball import Ball
from settings import Settings
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ball catching game")
    catcher = Character(ai_settings, screen)
    ball = Ball(ai_settings, screen)

    while True:
        gf.check_events(catcher)
        gf.update_screen(ai_settings, screen, catcher, ball)

run_game()