import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Класс для управления ресурсами и поведением игры """
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_widht, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)

	def run_game(self):
		# Запуск основного кода игры
		while True:
			self._check_events()
			# При каждом проходе цикла обновляется позиция корабля
			self.ship.update()
			# При каждом проходе цикла перерисовывается экран.
			self._update_screen()


	def _check_events(self):
		# Отслеживания событий клавы и мыши
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# переместить корабль вправо
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = True

			elif event.type == pygame.KEYUP:
				# переместить корабль вправо
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False

	def _update_screen(self):
		# Заполняем цветом фон, вызываем метод fill() с одним аргументом - цвет фона
			self.screen.fill(self.settings.bg_color)
			# рисуем корабль из модуля ship
			self.ship.blitme()
			# Отображение последнего отрисованного экрана
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()