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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:      # x btton commandto quit
                    sys.exit()

        
            #fill bg_color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


            #make last drawn screen visible
            pygame.display.flip()


        self.clock.tick(60)                    #a delay of 60th of a second or 60 times per second

if __name__=='__main__':
                                               #make game instance and run

    ai=AlienInvation()
    ai.run_game()


