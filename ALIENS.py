import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__ (self) -> None:
        """intialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        #set the screen based on settings
        if self.settings.fullscreen == True:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode\
                ((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.fleet = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")
        self.scoreboard = Scoreboard(self)

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._check_if_fleet_is_destroyed()
                self._update_aliens()
            self._update_screen()

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            else:
                self._check_keyup_events(event)
                self._check_keydown_events(event)

    def _check_play_button(self, mouse_pos: tuple) -> None:
        """A helper method to check if the player has clicked the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked == True and self.stats.game_active == False:
            #hide the mouse cursor
            pygame.mouse.set_visible(False)
            
            #resets values to the starting ones
            self.settings.init_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard._prep_score()
            self.scoreboard._prep_level()
            self.scoreboard._prep_ships()

            self.fleet.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()

    def _check_keyup_events(self, event) -> None:
        """Helper function for keyup events"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _check_keydown_events(self, event) -> None:
        """Helper function for keydown events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                self.ship.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _update_bullets(self) -> None:
        """A grouping of bullet related methods"""
        self.bullets.update()
        self._clean_up_bullets()
        self._bullet_collisions()
    
    def _bullet_collisions(self) -> None:
        #Check if any bullets have hit aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.fleet, True, True)

        #checks if there have been any collisions
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.check_high_score()
            self.scoreboard._prep_score()

    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_max_count:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _clean_up_bullets(self) -> None:
        """Checks if a bullet has gone over the upper border and removes it if so"""

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self) -> None:
        """A helper function to create a fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width -(2*alien_width)
        number_of_aliens_x = available_space_x // (2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height\
                            -(3*alien_height)-ship_height
        
        number_of_rows_y = available_space_y // (2*alien_height)

        for row_number in range(number_of_rows_y):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self) -> None:
        """Checks if fleet has reached an edge of the screen"""
        for alien in self.fleet.sprites():
            if alien.check_for_edges() == True:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Drops the entire fleet down and changes direction"""
        for alien in self.fleet.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_if_fleet_is_destroyed(self) -> None:
        """
        Checks if the fleet is destroyed,
        removes all the bullets and spawns a new
        fleet if it is
        """
        if not self.fleet:
            #increase level
            self.stats.level += 1
            self.scoreboard._prep_level()

            #increase speed
            self.settings.increase_speed()

            #clear the screen from bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self) -> None:
        """
        Check if the fleet is at an edge,
        then update the position of the fleet
        """
        self._check_fleet_edges()
        self.fleet.update()

        #Check if any aliens hit the ship
        if pygame.sprite.spritecollideany(self.ship, self.fleet):
            self._ship_hit()

        self._check_aliens_bottom()

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """A function to create a new alien whenever it is called"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.y = alien_height + (2*alien.rect.height*row_number)
        alien.rect.y = alien.y
        self.fleet.add(alien)

    def _ship_hit(self) -> None:
        """Respond to the ship being hit by an alien"""

        if self.stats.ships_left > 0:

            #decrement ships left and update scoreboard
            self.stats.ships_left -= 1
            self.scoreboard._prep_ships()

            self.fleet.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            #pause for a while
            sleep(0.5)
        else:
            self.stats.game_active = False
            #Set the mouse visible after dying
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self) -> None:
        """Checks if aliens have hit the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.fleet.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self) -> None:
        """Updates the screen each loop"""
        # Redraws the screen during each pass though the loop
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()

        #bullet drawing
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.fleet.draw(self.screen)

        # Draw the play button if the game state is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        # Draw the scoreboard
        self.scoreboard.draw_stats()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
