import sys

import pygame

from settings import Setttings


class AlienInvation:
    """overall class to manage game assetsand behavior"""

    def __init__(self):
        """initialise game and create game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()       #clock object for framerae controll

        self.settings=Setttings()              #settings class instance

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invation")    #window title

        self.bg_color=(180,180,180)          #a tuple fo rgb colors background color

    def run_game(self):
        """start main loop of the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:      # x btton commandto quit
                    sys.exit()

        
            #fill bg_color
            self.screen.fill(self.settings.bg_color)


            #make last drawn screen visible
            pygame.display.flip()


        self.clock.tick(60)                    #a delay of 60th of a second or 60 times per second

if __name__=='__main__':
                                               #make game instance and run

    ai=AlienInvation()
    ai.run_game()


