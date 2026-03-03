import sys
from time import sleep
import pygame
from character import Character
from ball import Ball


def check_keydown_events(event, character):
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True


def check_keyup_events(event, character):
    if event.key == pygame.K_RIGHT:
       character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False

def check_events(character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)

def update_game(character, ball, stats):
    character.update()
    ball.update()
    ball_collision(character, ball, stats)

def update_screen(ai_settings, screen, character, ball, stats):
    screen.fill(ai_settings.bg_color)
    character.blitme()
    ball.blitme()
    pygame.display.flip()

def ball_not_caught(character, ball, stats):
    if stats.character_left > 0:

        stats.character_left -= 1
        character.character_center()
        ball.reset_ball()
        sleep(0.5)
    else:
        stats.game_active = False



def ball_collision(character, ball, stats):
    if character.rect.colliderect(ball.rect):
        ball.reset_ball()
    elif ball.check_bottom():
        ball_not_caught(character, ball, stats)
