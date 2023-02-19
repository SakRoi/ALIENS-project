import pygame.font

class Button:

    def __init__(self, ai_game, msg) -> None:
        """Intializes the button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Dimensions and the properties of the button itself
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)