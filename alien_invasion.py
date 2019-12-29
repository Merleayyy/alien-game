# -*- coding: UTF-8 -*-
import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship,Charector

import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((
		ai_settings.screen_width, ai_settings.screen_height)) # 设置的窗口大小

	pygame.display.set_caption("Alien Invasion") # 窗口标题

	# 创建一艘飞船
	ship = Ship(ai_settings, screen)

	# 创建一个用于储存子弹的编组
	bullets = Group()

	# 创建一个2b
	# fighter = Charector(screen)

	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标的事件
		gf.check_event(ai_settings, screen, ship, bullets)

		#使飞船移动
		ship.update()
		#使子弹移动
		bullets.update()

		# 删除已经消失的子弹
		for bullet in bullets.copy():# 遍历保存子弹的编组，检索其是否已经射出屏幕
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))

		# 刷新屏幕
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game()
