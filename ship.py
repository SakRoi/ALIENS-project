import pygame

class Ship:
    """A simple class to represent an alien spaceship"""

    def __init__ (self, ai_game) -> None:
        """Intialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get it's rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Starts the ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Stores the ship's horizontal position in decimals
        self.x = float(self.rect.x)

        #Intialize settings
        self.settings = ai_game.settings

        #Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self) -> None:
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Updates rect object to be self.x
        self.rect.x = self.x

    
    def blitme(self) -> None:
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self) -> None:
        """
        Centers the ship
        mostly used to reset the ships position
        after getting destroyed
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

