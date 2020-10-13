import sys 
import pygame 
from time import sleep

from bullet import Bullet
from alien import Alien


def check_event(ai_settings, screen, ship, bullets):
    # 监视键盘和鼠标事件
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, screen, ai_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_keydown_event(event, screen, ai_settings, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allow:
        bullet = Bullet(screen, ai_settings, ship)
        bullets.add(bullet)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)

    # 显示最近绘制屏幕
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # remove bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_aliens_bullets_collision(ai_settings, screen, ship, aliens, bullets)
    
def check_aliens_bullets_collision(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens):
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    num_alien_x = get_num_aliens_x(ai_settings, alien.rect.width)
    num_alien_y = get_num_aliens_y(ai_settings, alien.rect.height, ship.rect.height)

    print("num alien x is = %d, num alien y is %d" % (num_alien_x, num_alien_y))
    for row_number in range(num_alien_y):
        for alien_num in range(num_alien_x):
            create_alien(ai_settings, aliens, screen, row_number, alien_num)

def get_num_aliens_x(ai_settings, alien_width):
    available_width = ai_settings.screen_width - alien_width * 2
    return int(available_width / (2 * alien_width))

def get_num_aliens_y(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, aliens, screen, row_number, alien_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_num
    
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    
    ai_settings.fleet_directions *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False