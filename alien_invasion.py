import sys, pygame
from settings import Settings

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) # my current screen dimension
    pygame.display.set_caption('Alien Invasion')

    # set the background color
    bg_color= (45, 56, 58)

    # start the main loop for the game
    running = True
    while running:

        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # different from Python Crash Course

        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        # make the most recently drawn screen visible
        pygame.display.flip()

    pygame.quit()

run_game()