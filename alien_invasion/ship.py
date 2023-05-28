import pygame

class Ship():
	# класс для управления кораблем (управляет всеми атрибутами корабля)
	def __init__(self, ai_game):
		# инициализирует корбаль и задает его начальную позицию
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = self.screen.get_rect()

		# загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship2.bmp')
		self.rect = self.image.get_rect()

		self.image_up = pygame.transform.rotate(self.image, 0)
		self.image_down = pygame.transform.rotate(self.image, -180)
		self.image_left = pygame.transform.rotate(self.image, 90)
		self.image_right = pygame.transform.rotate(self.image, -90)

		# каждый новый корабль у нижнего центра экрана midbottom
		self.rect.midbottom = self.screen_rect.midbottom

		# флаг перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# сохранение вещественной координаты корабля
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		# обновляется атрибут x, не rect
		# если moving_right == True
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		# обновляем атрибут на основании x
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		# рисует корабль в текущей позиции
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		"""Размещает корабль в центре нижней стороны"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
