import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # set the background color
    bg_color= ai_settings.bg_color

    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in 
    bullets = Group()

    # start the main loop for the game
    running = True
    while running:

        running = gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

    pygame.quit()

run_game()