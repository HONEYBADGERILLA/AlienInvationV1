import sys

import os

import pygame

from settings import Setttings

from ship import Ship

from bullet import Bullet

from alien import Alien

from time import sleep

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button



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

        #create an instance for statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)              #notice the self passed is the second self ie the game ai_game

        self.bullets = pygame.sprite.Group()  # like a list with extra functionality

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.bg_color=(180,180,180)          #a tuple fo rgb colors background color

        #start alien invation in game inactive state flag
        self.game_active = False
        self.play_pressed = False

        #make a play button and diff buttons
        self.play_button = Button(self, "Play")
        self.hard_button = Button(self,"hard","right")
        self.medium_button = Button(self, "medium")
        self.easy_button = Button(self,"easy", "left")


    def asset_path(self,*path_parts):
            """build path     focus folder with script this  """
            return os.path.join(os.path.dirname(__file__),"Assets",*path_parts) #focus folder on main file location, need research, * gives all sub and files


    def run_game(self):
        """start main loop of the game"""

        while True:
            
            self._check_events()

            if self.game_active:    
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

            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.play_pressed:
                    self._check_play_button(mouse_pos)
                else:
                    self._check_difficulty_buttons(mouse_pos)



    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos) #check if button clicked flag, in the button area
        if button_clicked and not self.game_active: 
           # reset if the game inactive and not when every time the btn area clicked

           self.stats.reset_stats()
           self.sb.prep_score()
           self.sb.prep_level()
           self.sb.prep_ships()
           
           self.play_pressed = True    #a flag for play button to move to diff button in update_screen


    def _check_difficulty_buttons(self, mouse_pos):
        """check diff buttons and init game as needed"""

        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_clicked or medium_clicked or hard_clicked and not self.game_active:
            if easy_clicked:
                self.settings.initialize_dynamic_settings(1)
                self._start_game()

            elif medium_clicked:
                self.settings.initialize_dynamic_settings()  #2 is standart no passing arg needed
                self._start_game()

            elif hard_clicked:
                self.settings.initialize_dynamic_settings(3)
                self._start_game()


    def _start_game(self):
        """start a new game instance"""

         #reset game stats give player new ships and such
        self.stats.reset_stats()
        self.game_active = True

        #get rid of any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        #create new fleet and center ship
        self._create_fleet()
        self.ship.center_ship()

        #hide mouse cursor after pressing play, its reset in ship hit method
        pygame.mouse.set_visible(False)
                

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

        elif event.key == pygame.K_p:
            if not self.game_active:
                self._start_game()


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

            self._check_bullet_alien_collitions()


    def _check_bullet_alien_collitions(self):
        #check for any bullets that have hit aliens
        #if so get rid of the bullet and the alien
        collition = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)

        if collition:
            for aliens in collition.values():          #make multi hit register by multiplying by number of members in dict
                self.stats.score += self.settings.alien__points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            

        if not self.aliens:
            #Destroy existing bullets and create new fleet

            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):

        """check edges and update pos of all aliens in fleet"""

        self._check_fleet_edges()
        self.aliens.update()    #called on a group so will call for each one

        #look for alien ship collitions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look or aliens at the screen bottom
        self._check_aliens_bottom()


    def _ship_hit(self):
        """respond to ship hit by alien"""

        if self.stats.ships_left >0:

            #decrement ships left and update scoreboard dash
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of sprites
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)  #reapear the cursor


    def _check_aliens_bottom(self):
        """check if any aliens got to the bottom"""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #treat as if ship got hit
                self._ship_hit()


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

        while current_y < (self.settings.screen_height - 5 * alien_height):

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

        #draw score info
        self.sb.show_score()
        
        self.ship.blitme()                         #draw ship

        if not self.game_active:
            if not self.play_pressed:
                self.play_button.draw_button()
            else:
                self.easy_button.draw_button()
                self.medium_button.draw_button()
                self.hard_button.draw_button()

        pygame.display.flip()                      #display last drawn screen


if __name__=='__main__':
    #make game instance and run

    ai=AlienInvation()
    ai.run_game()


