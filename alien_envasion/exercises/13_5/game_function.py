import sys
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

def update_screen(ai_settings, screen, character, ball):
    screen.fill(ai_settings.bg_color)
    character.update()
    character.blitme()
    ball.update()
    ball.blitme()
    pygame.display.flip()
    ball_collision(character, ball)


def ball_collision(character, ball):
    if character.rect.colliderect(ball.rect):
        ball.reset_ball()

    elif ball.check_bottom():
        ball.reset_ball()
