import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """create a single alien for a fleet"""

    def __init__(self,ai_game):
        """initialize an alien and set its startup location"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image and set rect
        self.image = pygame.image.load(ai_game.asset_path("octogreen.bmp"))
        self.rect = self.image.get_rect()

        #start new alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens exact horizontal pos
        self.x = float(self.rect.x)


    def update(self):
        """move the alien to the right or left"""

        self.x += self.settings.alien_speed * self.settings.fleet_direction  #1 or -1 multiplier depends on direction
        self.rect.x = self.x



    def check_edges(self):
        """return true if alien on screen edge"""

        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
