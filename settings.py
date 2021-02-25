class Settings:
    def __init__(self):
        #Screen stuff (switched to fullscreen, so like, whatever)
        self.screen_width: 1500
        self.screen_height = 800
        #Window background color
        self.bg_color = (0,0,0)
        #Ship stuff
        self.ship_speed = 1.5
        #LaZors
        self.laser_speed = 1.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (60,60,60)