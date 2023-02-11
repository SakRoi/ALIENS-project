import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    def __init__ (self, ai_game)-> None:
        """Intialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Spawn a new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self) -> None:
        self.x += self.settings.alien_speed
        self.rect.x = self.x
