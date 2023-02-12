import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""
    def __init__ (self, ai_game)-> None:
        """Intialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Spawn a new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_for_edges(self) -> bool:
        """Returns true if alien is next to an edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self) -> None:
        """Move the alien right or left"""
        self.x += (self.settings.alien_speed \
                   * self.settings.fleet_direction)
        self.rect.x = self.x
