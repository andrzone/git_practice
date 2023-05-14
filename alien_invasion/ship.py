import pygame

class Ship():
	# класс для управления кораблем (управляет всеми атрибутами корабля)
	def __init__(self, ai_game):
		# инициализирует корбаль и задает его начальную позицию
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# загружает изображение корабля и получает прямоугольник
		self.image = pygame.image.load('images/ship2.bmp')
		self.rect = self.image.get_rect()

		# каждый новый корабль у нижнего центра экрана
		self.rect.midbottom = self.screen_rect.midbottom

		# флаг перемещения
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# если moving_right == True
		if self.moving_right:
			self.rect.x +=1
		if self.moving_left:
			self.rect.x -=1

	def blitme(self):
		# рисует корабль в текущей позиции
		self.screen.blit(self.image, self.rect)
