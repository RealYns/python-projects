import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from target import Target
from ship import Ship
from button import Button
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("sideways shooter test")
    ship = Ship(ai_settings, screen)
    target = Target(ai_settings, screen)
    bullets = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")



    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button)
        if stats.game_active:
            ship.update()
            target.update()
            gf.update_bullets(ai_settings, bullets, target, stats)
        else:
            target.current_color = target.normal_color

        gf.update_screen(ai_settings, screen, ship, bullets, target, stats, play_button)

run_game()
