import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """player ship management class"""

    def __init__(self,ai_game):

        super().__init__()
        
        """init the ship and its first position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        #Load ship and get its rect(hitbox)
        self.image = pygame.image.load(ai_game.asset_path("Ship.bmp"))
        self.rect = self.image.get_rect()


        #start each new ship in bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #movement flags,start with no motion
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship position based on flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x=self.x



    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        """center the ship on screen"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)