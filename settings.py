
class Settings:
    """A class that stores all the settings for ALIENS"""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        #Screen settings
        self.fullscreen = True
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 100)

        #Alien's settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        
        #Ship's settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_max_count = 3
