import pygame
from pygame.sprite import Sprite

class Bullet_Pac(Sprite):
	"""Класс для управления выстрелами"""
	def __init__(self, pac_game):
		# для правильной реализации sprite:
		super().__init__()
		# создает объект снарядов в текущей позиции пакмена
		self.screen = pac_game.screen
		self.settings = pac_game.settings
		self.color = self.settings.bullet_color

		# создание снаряда в позиции 0 0 и перенос в правильную позицию

		self.rect = pygame.Rect(0,0,self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.center = pac_game.pac.rect.center

		# перевод позиции снаряда в вещественный тип
		self.x = self.rect.x

	def update(self):
		"""Перемещает снаряд по экрану"""
		# обновление позиции снаряда в вещественном формате
		self.x += self.settings.bullet_speed
		# обновление позиции снаряда
		self.rect.x = self.x


	def draw_bullet(self):
		# вывод снаряда на экран (рисуем)
		pygame.draw.rect(self.screen, self.color, self.rect)
