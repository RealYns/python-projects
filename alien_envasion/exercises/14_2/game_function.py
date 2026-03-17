import sys
from time import sleep
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, bullets, mouse_x, mouse_y)


def reset_game(ai_settings, screen, stats, ship, bullets, target):
    stats.reset_stats()
    stats.game_active = True

    bullets.empty()

    ship.rect.centery = ship.screen_rect.centery
    ship.center = float(ship.rect.centery)

    target.rect.centery = target.screen_rect.centery
    target.center = float(target.rect.centery)
    target.direction = 1


    pygame.mouse.set_visible(False)


def check_play_button(ai_settings, screen, stats, play_button, ship, bullets, mouse_x, mouse_y):

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        bullets.empty()
        ship.rect.centery = ship.screen_rect.centery
        ship.center = float(ship.rect.centery)
        pygame.mouse.set_visible(False)

def update_screen(ai_settings, screen, ship, bullets, target, stats, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    target.draw()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_settings, bullets, target, stats):
    bullets.update()
    check_bullet_target_collisions(target, bullets)

    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)
            target_missed(stats)

def check_bullet_target_collisions(target, bullets):
    for bullet in bullets.copy():
        if bullet.rect.colliderect(target.rect):
            bullets.remove(bullet)
            target.hit()


def target_missed(stats):
    if stats.ship_left > 0:
        stats.ship_left -= 1

        if stats.ship_left <= 0:
            stats.game_active = False
            pygame.mouse.set_visible(True)
        else:
            sleep(0.3)

