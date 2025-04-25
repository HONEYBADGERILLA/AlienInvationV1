import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """create a single alien for a fleet"""

    def __init__(self,ai_game):
        """initialize an alien and set its startup location"""

        super().__init__()
        self.screen = ai_game.screen

        #load alien image and set rect
        self.image = pygame.image.load(ai_game.asset_path("octogreen.bmp"))
        self.rect = self.image.get_rect()

        #start new alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens exact horizontal pos
        self.x = float(self.rect.x)