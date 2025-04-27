import sys

import os

import pygame

from settings import Setttings

from ship import Ship

from bullet import Bullet

from alien import Alien



class AlienInvation:
    """overall class to manage game assetsand behavior"""

    def __init__(self):
        """initialise game and create game resources"""

        pygame.init()

        self.clock = pygame.time.Clock()       #clock object for framerae controll

        self.settings=Setttings()              #settings class instance

        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invation")    #window title

        self.ship = Ship(self)              #notice the self passed is the second self ie the game ai_game

        self.bullets = pygame.sprite.Group()  # like a list with extra functionality

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.bg_color=(180,180,180)          #a tuple fo rgb colors background color


    def asset_path(self,*path_parts):
            """build path     focus folder with script this  """
            return os.path.join(os.path.dirname(__file__),"Assets",*path_parts) #focus folder on main file location, need research, * gives all sub and files


    def run_game(self):
        """start main loop of the game"""

        while True:
            
            self._check_events()
            
            self.ship.update()
            self._update_bullets()
            self._update_aliens() 
            self._update_screen() 

             
            self.clock.tick(60)                    #a delay of 60th of a second or 60 times per second


    def _check_events(self):
        """respond to keypress and mouse events"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  #cloe window with x button
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
               
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)      
                


    def _check_keydown_events(self,event):
        """respond to key press"""

        if event.key == pygame.K_RIGHT:
            #move ship right
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """respond to key release"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """create a new bullet and add it to the group"""

        if len(self.bullets) < self.settings.bullets_allowed:

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """update pos of bullets and erase old ones"""

        self.bullets.update()   #the sprite group will call the method on every bulled passed to it

        #get rid of bullets offscreen
        for bullet in self.bullets.copy(): #copy because loops work with fixed list size
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)


    def _update_aliens(self):
        """check edges and update pos of all aliens in fleet"""

        self._check_fleet_edges()
        self.aliens.update()    #called on a group so will call for each one


        
    def _create_alien(self,x_position, y_position):
        """create an alien and place it in the row"""

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """respond appropriately if any aliens reached the edges"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """drop entire fleet and change direction"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed  
        self.settings.fleet_direction *= -1


    def _create_fleet(self):
        """create a fleet of aliens"""

        #make an alien
        alien = Alien(self)
        
        #keep adding aliens until no room left
        #spacing between aliens is one width and one height

        alien_width,alien_height= alien.rect.size

        current_x , current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):

            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x , current_y)
                current_x += 2 * alien_width

            #finished a row: reset x and increment y values
            current_x = alien_width
            current_y += 2 * alien_height    
                


    def _update_screen(self):
        """update image on screen and flip to new screen"""

        self.screen.fill(self.settings.bg_color)   #fill background
        

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        
        self.ship.blitme()                         #draw ship

        pygame.display.flip()                      #display last drawn screen


if __name__=='__main__':
    #make game instance and run

    ai=AlienInvation()
    ai.run_game()


