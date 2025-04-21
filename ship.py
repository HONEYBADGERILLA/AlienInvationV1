import pygame

class Ship:
    """player ship management class"""

    def __init__(self,ai_game):
        """init the ship and its first position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        #Load ship and get its rect(hitbox)
        self.image = pygame.image.load(ai_game.asset_path("Ship.bmp"))
        self.rect = self.image.get_rect()


        #start each new ship in bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flags,start with no motion
        self.moving_right = False

    def update(self):
        """update ship position based on flags"""
        if self.moving_right:
            self.rect.x += 1



    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image,self.rect)