import sys

import os

import pygame

from settings import Setttings

from ship import Ship



class AlienInvation:
    """overall class to manage game assetsand behavior"""

    def __init__(self):
        """initialise game and create game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()       #clock object for framerae controll

        self.settings=Setttings()              #settings class instance

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invation")    #window title

        self.ship = Ship(self)              #notice the self passed is the second self ie the game ai_game

        self.bg_color=(180,180,180)          #a tuple fo rgb colors background color


    def asset_path(self,*path_parts):
            """build path     focus folder with script this  """
            return os.path.join(os.path.dirname(__file__),"Assets",*path_parts) #focus folder on main file location, need research, * gives all sub and files


    def run_game(self):
        """start main loop of the game"""

        while True:
            
            self._check_events()
            self._update_screen()
            self.ship.update()
            
            self.clock.tick(60)                    #a delay of 60th of a second or 60 times per second


    def _check_events(self):
        """respond to keypress and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #cloe window with x button
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move ship right
                    self.ship.moving_right = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                


    def _update_screen(self):
        """update image on screen and flip to new screen"""

        self.screen.fill(self.settings.bg_color)   #fill background
        self.ship.blitme()                         #draw ship

        pygame.display.flip()                      #display last drawn screen


if __name__=='__main__':
    #make game instance and run

    ai=AlienInvation()
    ai.run_game()


