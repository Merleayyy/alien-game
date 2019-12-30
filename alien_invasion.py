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

	# 创建一个2b
	# fighter = Charector(screen)

	localtime = time.localtime(time.time())
	localtime = time.strftime('%S', localtime)
	localtime = int(localtime)
	counter = 0

	# 开始游戏的主循环
	while True:
		
		# 监视键盘和鼠标的事件
		gf.check_event(ai_settings, screen, ship, bullets)


		# 生成外星人,每5秒生成一只外星人
		localtime = gf.show_aliens(ai_settings, aliens, screen,
		 localtime, counter)

		#创建好飞船之后更新飞船的坐标
		ship.update()

		gf.update_bullets(bullets)
		gf.update_aliens(aliens)

		# 刷新屏幕
		gf.update_screen(ai_settings, screen, ship, bullets, aliens)


		
run_game()

