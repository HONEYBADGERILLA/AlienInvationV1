import sys

import pygame


class AlienInvation:
    """overall class to manage game assetsand behavior"""

    def __init__(self):
        """initialise game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invation")

    def run_game(self):
        """start main loop of the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        #make last drawn screen visible
        pygame.display.flip()

if __name__=='__main__':
    #make game instance and run

    ai=AlienInvation()
    ai.run_game()


