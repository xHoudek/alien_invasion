import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """respond to keypresses and mouse events"""
    running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # different from Python Crash Course

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

    return running
                
def update_screen(ai_settings, screen, ship, bullets):
    """update images on the screen and flip to the new screen"""
    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # make the most recently drawn screen visible
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to keypresses"""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
    # update bullet positions
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached yet"""
    # create a new bullet and add it to the bullets groups
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)