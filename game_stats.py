class GameStats:
    """Track statistics for ALIENS"""

    def __init__ (self, ai_game) -> None:
        """Intial Statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start ALIENS in an inactive state
        self.game_active = False

    def reset_stats(self) -> None:
        """Intialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

