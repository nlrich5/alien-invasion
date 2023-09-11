class Settings:
    # A class to store settings for the game

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Fleet direction (1 = right, -1 = left)
        self.fleet_direction = 1

        # Background settings
        self.star_speed = 2
        self.star_size = 5


