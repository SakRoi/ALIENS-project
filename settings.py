
class Settings:
    """A class that stores all the settings for ALIENS"""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        #Screen settings
        self.fullscreen = True
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 100)
        
        #Ship's settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_max_count = 3
