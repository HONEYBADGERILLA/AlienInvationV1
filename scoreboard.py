import pygame.font

from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """a class to report scoring info"""

    def __init__(self, ai_game):
        """init scoreboard attributes"""

        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats


        """font settings for scoring info"""
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #prep score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):

        """turn score to a rendered image"""

        rounded_score = round(self.stats.score, -1)    # -1 value passed means rounding to nearest 10 100 1000 
        score_str = f"{rounded_score:,}"               # f string formatting ";," means insert commas in numbers as needed so 9,020 will see
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)


        """display score on topright of screen"""
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """turn highscore to rendered image"""

        high_score = round(self.stats.high_score,-1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #center the highscore at top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        

    def prep_ships(self):
        """show how many ships left"""

        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (30,30))        #rescale the ship instance by acessing class attributes
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        """draw score to screen"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)


    def check_high_score(self):
        """check to see if the new score is highest"""

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """playr level dash score"""

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



        
