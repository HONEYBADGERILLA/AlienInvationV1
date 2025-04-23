import pygame 
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""


    def __init__(self, ai_game):
        """create a bullet object at ships current location"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.color = self.settings.bullet_color

        """create a bullet rect at 0 0 and then move to ship pos"""
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop


        """store bullet location as float"""
        self.y = float(self.rect.y)


    def update(self):
        """move bullet up the screen"""
        self.y -= self.settings.bullet_speed #update exact pos of bullet
        self.rect.y = self.y                 #update the rectangle


    def draw_bullet(self):
        """draw bullet to screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
