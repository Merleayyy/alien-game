# -*- coding: UTF-8 -*-
import pygame
from settings import Settings


class Ship():
	def __init__(self, ai_settings, screen):
		# 初始化飞船并设置其初始的位置
		self.screen = screen

		# 获取到飞船的各种属性
		self.ai_settings = ai_settings

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.jpeg')
		self.rect = self.image.get_rect() # 获取图片的矩形
		self.screen_rect = screen.get_rect() # 获取屏幕的矩形

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx #设置图片矩形的位置
		self.rect.bottom = self.screen_rect.bottom #同上

		# 在飞船的属性中存储小数值
		self.center = float(self.rect.centerx)

		# 移动标志
		self.moving_left = False
		self.moving_right = False

	def update(self):
		# 更新飞船的坐标
		if self.moving_right == True and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_left == True and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed

		# 使用小数值来设置飞船的位置
		self.rect.centerx = self.center

	def blitme(self):
		# 在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)

class Charector(object):
	"""docstring for Charctor"""
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/2b.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		