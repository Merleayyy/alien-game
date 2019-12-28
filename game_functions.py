# -*- coding: UTF-8 -*-
import sys
import pygame
def check_event(ship):
	# 响应按键和鼠标的事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def check_keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# 确保按下按键时，飞船处于一种移动的状态
		ship.moving_right = True

	if event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
		
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, fighter):
	# 每次循环时都设置屏幕为bg_color的颜色
	screen.fill(ai_settings.bg_color)
	# 在屏幕上绘制飞船的图片
	ship.blitme()
	fighter.blitme()
	# 让最近绘制的屏幕可见
	pygame.display.flip() # 使用之前设置好的属性，一遍一遍绘制图像
