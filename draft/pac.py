import pygame

class Pac():
	"""Класс для управления паком"""
	def __init__(self, pac_game):
		# обращаемся ко всему экрану
		self.screen = pac_game.screen
		# создаем атрибут settings_pac, чтобы его использовать в update
		self.settings = pac_game.settings
		# позволяет разместить изображение в нужной позиции
		self.screen_rect = pac_game.screen.get_rect()

		# загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('image/pac.png')
		# получаем ссылку на размеры этой области в виде /экземпляра класса Rect
		self.rect = self.image.get_rect()
		# каждый новый pac будет выравниваться в середине экрана
		self.rect.midleft = self.screen_rect.midleft

		# сохранение вещественной координаты цетра героя
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		# флаг перемещения
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def blitme(self):
		"""Рисует изображение в текущей позиции"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Обновляет позицию корабля с учетом флага"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.pac_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.pac_speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.pac_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.pac_speed

		self.rect.x = self.x
		self.rect.y = self.y

