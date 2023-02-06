import pygame
from pygame import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    def __init__ (self, ai_game):
        """Intialize the alien and set it's starting position"""
        super().__init()
        self.screen = ai_game.screen

        # Load the alien and set its rect attribute.
        self.image = pygames.image.load("images.alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)