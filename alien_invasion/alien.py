import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Класс, представляющий одного прищельца"""
	def __init__(self,ai_game):
		"""Инициализирует пришельца и задает его изначальную позицию"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		# self.screen_rect = ai_game.screen.get_rect()

		# загружает корабль
		self.image = pygame.image.load('images/nlo.png')
		self.rect = self.image.get_rect()

		# каждый новый пришелец в вверхнем левом углу экрана
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# сохранение точной горизонтальной позиции пришельца
		self.x = float(self.rect.x)

	def update(self):
		# Перемещает пришельца вправо или влево
		self.x += (self.settings.alien_speed *
			self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""Возвращает True, если пришелец у края экрана"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True