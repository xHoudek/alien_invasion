import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # create an instance to store game statistics
    stats = GameStats(ai_settings)

    # set the background color
    bg_color= ai_settings.bg_color

    # make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    running = True
    while running:
        running = gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    pygame.quit()

run_game()