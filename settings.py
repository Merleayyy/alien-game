# -*- coding: UTF-8 -*-
class Settings():
	# 储存《外星人入侵》的所有设置的类
	def __init__(self):
		# 初始化游戏的设置

		# 屏幕的设置
		self.screen_width = 1600
		self.screen_height = 900
		self.bg_color = (20, 90, 160)
		# 设置飞船速度
		self.ship_speed = 7.1

		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
