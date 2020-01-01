# -*- coding: UTF-8 -*-
import pygame
from settings import Settings
from pygame.sprite import Sprite
import random

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		# 初始化飞船并设置其初始的位置
		self.screen = screen

		# 获取到飞船的各种属性
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect() # 获取图片的矩形
		self.screen_rect = screen.get_rect() # 获取屏幕的矩形


		# 在飞船的属性中存储小数值
		self.center = float(self.rect.centerx)

		# 将每艘新外星人放到屏幕之外
		self.rect.top = -self.rect.height #设置图片矩形的位置
		self.start = False # 检测外星人是否开始下落
		self.alien_number = 0


	def update(self):
		if self.start == False:
			self.alien_number = random.randint(1, 50)
			self.start = True
		self.rect.centerx = 29 * self.alien_number
		# 更新飞船的坐标
		if self.rect.centerx < 0:
			self.rect.top = 0
			self.rect.bottom = self.rect.height
		else:
			self.center += self.ai_settings.alien_speed_factor

		self.rect.centery = self.center

	def blitme(self):
		# 在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)


	def draw_alien(self):
		# 在屏幕上绘制子弹
		pygame.draw.rect(self.screen, self.color, self.rect)