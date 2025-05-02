
class GameStats:
    """track statistics for alien invation game"""

    def __init__(self,ai_game):
        """init the stats"""

        self.settings = ai_game.settings
        self.reset_stats()

        #highscore dont never reset
        self.high_score = 0


    def reset_stats(self):
        """init stats that change over and during game"""
        
        self.ships_left = self.settings.ship_limit

        self.score = 0
        self.level = 1

        