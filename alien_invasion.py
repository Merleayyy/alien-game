# -*- coding: UTF-8 -*-
import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship,Charector

import game_functions as gf

import random

from alien import Alien

import time

from game_stats import GameStats

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((
		ai_settings.screen_width, ai_settings.screen_height)) # 设置的窗口大小

	pygame.display.set_caption("Alien Invasion") # 窗口标题

	# 创建一艘飞船
	ship = Ship(ai_settings, screen)

	# 创建一个外星人
	aliens = Group()

	# 创建一个用于储存子弹的编组
	bullets = Group()

	localtime = time.localtime(time.time())
	localtime = time.strftime('%S', localtime)
	localtime = int(localtime)
	counter = 0

	# 创建一个用于储存游戏统计信息的实例
	stats = GameStats(ai_settings)
	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标的事件
		gf.check_event(ai_settings, screen, ship, bullets)


		if stats.game_active:

		# 生成外星人,每5秒生成一只外星人
			localtime = gf.show_aliens(ai_settings, aliens, screen,
		 localtime, counter)


			#创建好飞船之后更新飞船的坐标
			ship.update()

			gf.update_bullets(aliens, bullets)

			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			if ai_settings.dead_alive == True:
				current_time = time.localtime(time.time())
				current_time = time.strftime('%S', current_time)
				current_time = int(current_time)
				localtime = current_time
				ai_settings.dead_alive = False


		# 刷新屏幕
		gf.update_screen(ai_settings, screen, ship, bullets, aliens)


		
run_game()

