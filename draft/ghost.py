import pygame

class Ghost():
	"""Класс для управления ghost"""
	def __init__(self, pac_game):
		"""обращаемся ко всему экрану"""
		self.screen = pac_game.screen
		# позволяет разместить изображение в нужной позиции
		self.screen_rect = pac_game.screen.get_rect()

		# загружаем изображение
		self.image = pygame.image.load('image/ghost.png')
		# получаем ссылку на размеры этой области в виде /экземпляра класса Rect
		self.rect = self.image.get_rect()
		# изначальное местоположение на экране
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""отображение на экране в текущей позиции"""
		self.screen.blit(self.image, self.rect)
