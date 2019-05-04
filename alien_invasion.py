import sys, pygame
from settings import Settings
from ship import Ship

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
    ship = Ship(screen)

    # start the main loop for the game
    running = True
    while running:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # different from Python Crash Course

        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()

    pygame.quit()

run_game()