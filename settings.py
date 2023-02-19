
class Settings:
    """A class that stores all the settings for ALIENS"""

    def __init__(self) -> None:
        """Initializes the game's static settings."""
        #Screen settings
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 100)

        #Ship's settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_max_count = 3

        #Speed up settings
        self.speedup_scale = 1.1

        #Point up settings
        self.extra_points = 10

        self.init_dynamic_settings()

    def init_dynamic_settings(self) -> None:
        """Initializes the game's dynamic settings"""

        #Alien's settings
        self.alien_points = 50
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #Ship's settings
        self.ship_speed = 1.5

        #Bullet's settings
        self.bullet_speed = 1.0

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
    
    def increase_speed(self) -> None:
        """Increases speed settings"""
        
        #Player's settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        #Alien's settings
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points += self.extra_points
