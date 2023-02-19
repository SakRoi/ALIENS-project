import pygame.font

class Button:

    def __init__(self, ai_game, msg:str) -> None:
        """Intializes the button's attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Dimensions and the properties of the button itself
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #Builds the buttons rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(msg: str) -> None:
        """"""