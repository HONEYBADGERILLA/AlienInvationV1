class Setttings:
    """all the settings class for aigame"""

    def __init__(self):
        """initialise the game static settings"""
        #Screen Settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(120,120,120)

        #Ship settings
        self.ship_limit = 3

        #Bulet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,60)
        self.bullets_allowed = 5

        #alien settings
        self.fleet_drop_speed = 10   


        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self, difficulty=2):
        """init settins that change through the game"""

        if difficulty==1:
            self.ship_speed = 10
            self.bullet_speed = 20
            self.alien_speed = 1.5
            #how fast aliens speed up
            self.speedup_scale = 1.1

        elif difficulty==2:
            self.ship_speed = 6
            self.bullet_speed = 8
            self.alien_speed = 2.5
            #how fast aliens speed up
            self.speedup_scale = 1.3

        elif difficulty==3:
            self.ship_speed = 6
            self.bullet_speed = 8
            self.alien_speed = 5
            #how fast aliens speed up
            self.speedup_scale = 1.5

        self.fleet_direction = 1     #1 for right -1 for left for x multiplier

        #score settings
        self.alien__points = 50


    def increase_speed(self):
        """increase speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


