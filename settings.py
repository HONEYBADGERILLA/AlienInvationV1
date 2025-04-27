class Setttings:
    """all the settings class for aigame"""

    def __init__(self):
        
        #Screen Settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(120,120,120)

        #Ship settings
        self.ship_speed = 5

        #Bulet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,60)
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1     #1 for right -1 for left for x multiplier


