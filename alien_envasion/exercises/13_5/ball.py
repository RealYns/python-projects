import pygame
from pygame.sprite import Sprite
import random

class Ball(Sprite):

    def __init__(self, ai_settings, screen):

        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        original_image = pygame.image.load('finger.jpg')

        desired_width = 40
        desired_height = 40

        self.image = pygame.transform.scale(original_image, (desired_width, desired_height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.reset_ball()

        self.y = float(self.rect.y)

    def reset_ball(self):
        self.rect.x = random.randint(0, self.ai_settings.screen_width - self.rect.width)
        self.rect.y = 0
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y +=  self.ai_settings.ball_drop_speed
        self.rect.y = self.y

    def check_bottom(self):
        return self.rect.top >= self.ai_settings.screen_height