import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__ (self):
        """intialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.background_color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraws the screen during each pass though the loop
            self.screen.fill(self.background_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()