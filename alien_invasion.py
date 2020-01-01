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

from button import Button

from record import Record

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((
		ai_settings.screen_width, ai_settings.screen_height)) # 设置的窗口大小

	pygame.display.set_caption("Alien Invasion") # 窗口标题

	# 创建Play按钮
	play_button = Button(ai_settings, screen, "PLAY")

	# 创建一个计分板
	counter = '0'
	record_border = Record(ai_settings, screen)


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

		# 当游戏尚未开始时，持续记录系统时间，当开始后则开始正常系统运行，跳过此项
		localtime = gf.get_localtime(stats, localtime)

		# 监视键盘和鼠标的事件
		gf.check_event(ai_settings, screen, ship, bullets, 
			stats, play_button, aliens)


		if stats.game_active:

		# 生成外星人,每5秒生成一只外星人
			localtime = gf.show_aliens(ai_settings, aliens, screen,
		 localtime, counter)


			#创建好飞船之后更新飞船的坐标
			ship.update()
			# 实时更新子弹的坐标
			gf.update_bullets(aliens, bullets, record_border)
			# 实时更新外星人的坐标
			gf.update_aliens(ai_settings, stats, screen, 
				ship, aliens, bullets, record_border)
			
			# 在飞船生命用完之后，持续记录本地时间，不然无法生成新的外星人
			if ai_settings.dead_alive == True:
				# 飞船死亡
				current_time = time.localtime(time.time())
				current_time = time.strftime('%S', current_time)
				current_time = int(current_time)
				localtime = current_time
				# 避免无法生成新的外星人
				if localtime >= 57:
					localtime = 0
				ai_settings.dead_alive = False


		# 刷新屏幕
		gf.update_screen(ai_settings, screen, stats, ship, 
			bullets, aliens, play_button, record_border)


		
run_game()

