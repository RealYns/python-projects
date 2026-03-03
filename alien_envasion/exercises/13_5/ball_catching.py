import pygame
from character import Character
from game_stats import GameStats
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
    stats = GameStats(ai_settings)

    while True:
        gf.check_events(catcher)
        if stats.game_active:
            gf.update_game(catcher, ball, stats)

        gf.update_screen(ai_settings, screen, catcher, ball, stats)

run_game()