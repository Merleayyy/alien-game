import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""

	def __init__(self, ai_sittings, screen, ship):
		# 在飞船所处的位置创建一个子弹对象
		super(Bullet, self).__init__()
		self.screen = screen

		# 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
		# 根据设置创建矩形
		self.rect = pygame.Rect(0, 0, ai_sittings.bullet_width, ai_sittings.bullet_height)
		# 设置矩形（子弹）出现的位置
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 储存使用小数表示的子弹位置
		self.y = float(self.rect.y)
		self.color = ai_sittings.bullet_color
		self.speed_factor = ai_sittings.bullet_speed_factor

		# 创建一个用于显示可用子弹数的计数板
		# self.counting_border = pygame.Rect(ai_sittings.border_x, ai_sittings.border_y, 
		# 	ai_sittings.border_width, ai_sittings.border_height)
	
	def update(self):
		# 想上移动子弹
		# 更新表示子弹位置的小数值
		self.y -= self.speed_factor
		# 更新表示子弹的rect的数值
		self.rect.y = self.y


	def draw_bullet(self):
		# 在屏幕上绘制子弹
		pygame.draw.rect(self.screen, self.color, self.rect)