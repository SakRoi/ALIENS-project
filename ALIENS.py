import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__ (self):
        """intialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else: 
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
    
    def _check_events(self) -> None:
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                self._right_movement_checker(event)
                self._left_movement_checker(event)
    
    def _check_keyup_events(self, event) -> None:
        """Helper function for moving the spaceship right"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:
        """Helper function for keydown events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                self.ship.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
 
    def _update_screen(self) -> None:
        """Updates the screen each loop"""
        # Redraws the screen during each pass though the loop
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()