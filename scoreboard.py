import pygame.font

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game) -> None:
        """Intialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings for the screen
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the intial score screen
        self._prep_score()

    def _prep_score(self) -> None:
        """Renders the scoreboard"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self) -> None:
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)