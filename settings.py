
class Settings:
    """A class that stores all the settings for ALIENS"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 100)
        
        #Ship's settings
        self.ship_speed = 1.5