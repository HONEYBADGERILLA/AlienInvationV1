import pygame

class Ship:
    """player ship management class"""

    def __init__(self,ai_game):
        """init the ship and its first position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        #Load ship and get its rect(hitbox)
        self.image = pygame.image.load("Assets/Ship.bmp")
        self.rect = self.image.get_rect()


        #start each new ship in bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image,self.rect)