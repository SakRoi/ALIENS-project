import pygame

class Ship:
    """A simple class to represent an alien spaceship"""

    def __init__ (self, ai_game):
        """Intialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get it's rect.
        self.image = pygame.image.load("images/ship.bmp")
        