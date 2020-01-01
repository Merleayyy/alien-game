# -*- coding: UTF-8 -*-
import sys
import pygame
from bullet import Bullet
import random
from alien import Alien
import time
from time import sleep
def check_event(ai_settings, screen, ship, bullets):
	# 响应按键和鼠标的事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, ai_settings, screen, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def check_keydown_events(event, ship, ai_settings, screen, bullets):
	if event.key == pygame.K_RIGHT:
		# 确保按下按键时，飞船处于一种移动的状态
		ship.moving_right = True

	if event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key == pygame.K_SPACE:
		# 创建一颗子弹，并将其加入到编组bullet中
		fire_bullet(ai_settings, screen, ship, bullets)
# 发射子弹，按空格后创建一个子弹类
def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def show_aliens(ai_settings, aliens, screen, sec, counter):
	current_time = time.localtime(time.time())
	current_time = time.strftime('%S', current_time)
	current_time = int(current_time)
	print("当前时间为" + str(current_time))
	print("开始时间为" + str(sec))
	if current_time == sec + 3:
		new_alien = Alien(ai_settings, screen)
		aliens.add(new_alien)
		sec = current_time
		if sec >= 57:
			sec = 0
			return sec
		return sec
	return sec



# 监听鼠标回落的事件
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
		
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets, aliens):
	# 每次循环时都设置屏幕为bg_color的颜色
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	for alien in aliens.sprites():
		alien.blitme()

	# 在屏幕上绘制飞船的图片
	ship.blitme()
	# fighter.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip() # 使用之前设置好的属性，一遍一遍绘制图像

def update_bullets(aliens, bullets):
	# 更新子弹的位置，并且删除已经消失的子弹
	#使子弹移动
	bullets.update()

	# 删除已经消失的子弹
	for bullet in bullets.copy():# 遍历保存子弹的编组，检索其是否已经射出屏幕
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# print(len(bullets))

	# 检查是否有子弹击中了外星人
	# 如果是这样，就删除了相应的子弹和外星人
	collosions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# 

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	aliens.update()

	# 删除已经消失的外星人
	for alien in aliens.copy():# 遍历保存子弹的编组，检索其是否已经射出屏幕
		if alien.rect.top > 900:
			aliens.remove(alien)
	# 检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
		ai_settings.dead_alive = True

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	# 响应被外星人撞到的飞船
	if stats.ships_left > 0:
		stats.ships_left -= 1
		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 重置飞船位置
		ship.center_ship()

		sleep(1)
	else:
		stats.game_active =False
