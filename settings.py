class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initializes the game's settings"""
        # screen settings
        self.screen_width = 1366
        self.screen_height = 709
        self.bg_color = (45, 56, 58)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 250, 250
        self.bullets_allowed = 3