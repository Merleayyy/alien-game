# -*- coding: UTF-8 -*-
import sys

import pygame

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

	# 创建一个2b
	fighter = Charector(screen)

	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标的事件
		gf.check_event(ship)

		#使飞船移动
		ship.update()

		# 刷新屏幕
		gf.update_screen(ai_settings, screen, ship, fighter)
		
run_game()
