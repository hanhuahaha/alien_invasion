import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    #响应按键落下
    if event.key == pygame.K_d:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_a:
        #向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_RETURN:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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

def fire_bullet(ai_settings, screen, ship, bullets):
    #如果未达到限制就发射一枚子弹
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(aliens, bullets):
    #g更新子弹位置，并消除以消失的子弹
    #更新子弹位置
    bullets.update()
    #删除以消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    #检查是否有子弹击中了外星人
    #如果是这样，就删除相应的子弹和外星人
    cllisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
def get_number_aliens_x(ai_settings, alien_width):
    #计算每行可容纳多少个外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_rows(ai_settings, ship_height, alien_height):
    #计算屏幕可容纳多少行外星人
    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #创建一个外星人并将其放入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    #创建外星人群
    #创建一个外星人，并计算第一行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_aliens_rows(ai_settings, ship.rect.height, alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edge(ai_settings, aliens):
    #有外星人到达边缘时采取相应的措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #将整群外星人下移，并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    #检查是否有外星人位于屏幕边缘，更新外星人所在的位置
    check_fleet_edge(ai_settings, aliens)
    aliens.update()

def update_screen(ai_settings, screen, ship, bullets, aliens):
    #更新屏幕上的图像
    #每次循环时都重绘屏幕
    #填充屏幕背景色
    screen.fill(ai_settings.bg_color)
    #绘制飞船
    ship.blitme()
    #绘制外星人
    aliens.draw(screen)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    #让最近绘制的屏幕可见
    pygame.display.flip()

