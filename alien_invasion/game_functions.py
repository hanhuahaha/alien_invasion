import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    #响应按键落下
    if event.key == pygame.K_d:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_a:
        #向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_RETURN:
        #创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event,ship):
    #响应按键弹起
    if event.key == pygame.K_d:
        #停止向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_a:
        #停止向左移动飞船
        ship.moving_left = False

def check_events(ship, ai_settings, screen, bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_bullets(bullets):
    #g更新子弹位置，并消除以消失的子弹
    #更新子弹位置
    bullets.update()
    #删除以消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    #更新屏幕上的图像
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    #让最近绘制的屏幕可见VCXZ
    pygame.display.flip()

