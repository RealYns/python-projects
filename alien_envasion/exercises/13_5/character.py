import pygame


class Character():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        original_image = pygame.image.load('thukuna.jpg')

        desired_width = 80
        desired_height = 80

        self.image = pygame.transform.scale(original_image, (desired_width, desired_height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.character_speed

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def character_center(self):
        self.center = self.screen_rect.centerx

