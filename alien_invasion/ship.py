import pygame

class Ship():
	# класс для управления кораблем (управляет всеми атрибутами корабля)
	def __init__(self, ai_game):
		# инициализирует корбаль и задает его начальную позицию
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship2.bmp')
		self.rect = self.image.get_rect()

		# каждый новый корабль у нижнего центра экрана
		self.rect.midbottom = self.screen_rect.midbottom

		# флаг перемещения
		self.moving_right = False
		self.moving_left = False

		# сохранение вещественной координаты корабля
		self.x = float(self.rect.x)

	def update(self):
		# обновляется атрибут x, не rect
		# если moving_right == True
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.ship_speed
		# обновляем атрибут на основании x
		self.rect.x = self.x

	def blitme(self):
		# рисует корабль в текущей позиции
		self.screen.blit(self.image, self.rect)
