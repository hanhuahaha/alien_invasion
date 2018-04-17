import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

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


    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        #更新飞船位置
        ship.update()
        #更新屏幕图像并保持可见
        gf.update_screen(ai_settings,screen,ship)
run_game()