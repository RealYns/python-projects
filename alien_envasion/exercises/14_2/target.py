import pygame


class Target():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, 200, 150)
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.center = float(self.rect.centery)

        self.hit_color = (255, 255, 255)
        self.hit_flash_duration = 0
        self.normal_color = (255, 0, 0)
        self.current_color =self.normal_color

    def update(self):
        self.center += self.ai_settings.target_speed_factor * self.ai_settings.direction
        self.rect.centery = self.center

        if self.rect.bottom >= self.screen_rect.bottom:
            self.ai_settings.direction = -1
        elif self.rect.top <= self.screen_rect.top:
            self.ai_settings.direction = 1

        if self.hit_flash_duration > 0:
            self.hit_flash_duration -= 1
            self.current_color = self.hit_color
        else:
            self.current_color = self.normal_color

    def hit(self):
        self.hit_flash_duration = 10
        print("Target hit!")


    def draw(self):
        pygame.draw.rect(self.screen, self.current_color, self.rect)



