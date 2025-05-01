import pygame.font

class Button:
    """build buttons for the game"""

    def __init__(self,ai_game, msg, position = "center"):
        
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()


        """set dimeentions and properties for the button"""
        self.width, self.height = 200, 50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        """build button rect obj and render it"""
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        if position == "center":
            self.rect.center = self.screen_rect.center
        elif position == "right":
            self.rect.center = self.screen_rect.center
            self.rect.x = (self.rect.x + self.width + 60) 
        elif position == "left":
            self.rect.center = self.screen_rect.center
            self.rect.x = (self.rect.x - self.width - 60) 

        """the button needs to be prepped only once"""
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """turn msg in to a rendered image and center it on the button"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center



    def draw_button(self):
        """draw blank button and then draw mwssage"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
