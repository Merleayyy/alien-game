# -*- coding: UTF-8 -*-
import sys
import pygame
from bullet import Bullet
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

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
		
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
	# 每次循环时都设置屏幕为bg_color的颜色
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 在屏幕上绘制飞船的图片
	ship.blitme()
	# fighter.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip() # 使用之前设置好的属性，一遍一遍绘制图像

def update_bullets(bullets):
	# 更新子弹的位置，并且删除已经消失的子弹
	#使子弹移动
	bullets.update()

	# 删除已经消失的子弹
	for bullet in bullets.copy():# 遍历保存子弹的编组，检索其是否已经射出屏幕
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))
