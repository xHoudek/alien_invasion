class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initializes the game's static settings"""
        # screen settings
        self.screen_width = 1366
        self.screen_height = 709
        self.bg_color = (0, 59, 89)
            # space gray: (45, 56, 58)
            # space blue: (0, 59, 89)
            # sky blue: (135, 206, 235)

        # ship settings
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 3
            # normal: 3
            # superwide: 300
        self.bullet_height = 15
        self.bullet_color = 255, 255, 102
            # white: 250, 250, 250
            # yellow: 255, 255, 102
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.3
        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 6
        self.alien_speed_factor = 1

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings and alien point values"""
        #self.ship_speed_factor *= self.speedup_scale
        #self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)