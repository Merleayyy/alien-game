import pygame.font
class Record():
	"""创建带标签的实心矩形"""
	def __init__(self, ai_settings, screen):
		# 初始换按钮的属性
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# 设置按钮的尺寸和其他属性
		self.width, self.height = 200, 50
		self.record_color = (0, 255, 0)
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		# 创建按钮的rect对象，并使其居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.right = self.screen_rect.right
		self.rect.top = 0
		self.counter = '0'
		# 按钮的标签只需创建一次
		self.prep_msg(self.counter)

	def prep_msg(self, counter):
		# 将msg渲染为图像，并使其在按钮上居中
		self.msg_image = self.font.render(counter, True, 
			self.text_color, self.record_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# 绘制一个颜色填充的按钮，然后再绘制文本
		self.screen.fill(self.record_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def update_record(self):
		self.counter = str(1 + int(self.counter))


	def update_record_zero(self):
		self.counter = '0'
