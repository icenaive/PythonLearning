import pygame 
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 屏幕颜色
    # bg_color = (6, 47, 74)
    pygame.display.set_caption("Alien Invasion")
    # 创建ship
    ship = Ship(screen, ai_settings)
    ## 
    bullets = Group()
    ## 
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()