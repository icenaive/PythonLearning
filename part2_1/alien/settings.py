class Settings():
    """保存设置信息"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 3
        # alien 
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_directions = 1
