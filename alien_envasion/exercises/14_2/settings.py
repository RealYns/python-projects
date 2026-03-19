class Settings():

    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bullet_width = 20
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.direction = 1
        self.ship_lives = 3
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.target_speed_factor = 1


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale
