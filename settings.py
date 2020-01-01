# -*- coding: UTF-8 -*-
class Settings():
	# 储存《外星人入侵》的所有设置的类
	def __init__(self):
		# 初始化游戏的设置

		# 屏幕的设置
		self.screen_width = 1600
		self.screen_height = 900
		self.bg_color = (255, 255, 255)
		# 设置飞船属性
		self.ship_speed = 3
		self.ship_limit = 1

		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 50

		# # 计数板设置
		# self.border_x = 1500
		# self.border_y = 100
		# self.border_width = 100
		# self.border_height = 100

		# 外星人飞船的属性
		self.alien_speed_factor = 2

		# 判断是否死亡的标识
		self.dead_alive = False

		# 积分版属性