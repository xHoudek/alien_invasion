class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initializes the game's settings"""
        # screen settings
        self.screen_width = 1366
        self.screen_height = 709
        self.bg_color = (0, 59, 89)
        # space gray: (45, 56, 58)
        # space blue: (0, 59, 89)
        # sky blue: (135, 206, 235)

        # ship settings
        self.ship_speed_factor = 2.5

        # bullet settings
        self.bullet_speed_factor = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 102
        # white: 250, 250, 250
        # yellow: 255, 255, 102

        self.bullets_allowed = 5