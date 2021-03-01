import sys
from settings import Settings
import pygame
from ship import Ship
from laser import Laser
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("My game")
        self.ship = Ship(self)
        self.lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()        
            
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings .screen_width - (2 * alien_width)
        number_of_aliens_x =  available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for rows in range(number_rows) :       
            for alien_number in range(number_of_aliens_x):
                alien = Alien(self)
                alien.x = alien_width + 2 * alien_width * alien_number
                alien.rect.x = alien.x 
                alien.rect.y = alien.rect.height + 2 *alien.rect.height + rows
                self.aliens.add(alien)

    def fire_laser(self):
        new_laser = Laser(self)
        self.lasers.add(new_laser)  
    
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_laser() 
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.lasers.update()
            #Need to copy list because the length of the list can't change when running the for loop,
            #and so I copy the list and remove the corresponding bullet from the actual list.
            for laser in self.lasers.copy():
                if laser.rect.bottom <=0:
                    self.lasers.remove(laser)
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()