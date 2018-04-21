import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏
    pygame.init()
    #创建设置实例
    ai_settings = Settings()
    #创建屏幕实例
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #创建飞船实例
    ship = Ship(screen,ai_settings)
    #显示标题
    pygame.display.set_caption("Alien_Invasion")
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    #创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #创建一个用于存储游戏统计信息的实例和一个记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #创建一个button实例
    play_button = Button(ai_settings, screen, "Play")
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets, aliens, stats, play_button,)

        if stats.game_active:
            #更新飞船位置
            ship.update()
            #更新子弹位置并删除已消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            #更新外星人所在的位置
            gf.update_aliens(ai_settings, screen, ship, bullets, aliens, stats)
        #更新屏幕图像并保持可见
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)

run_game()