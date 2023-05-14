import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Класс для управления ресурсами и поведением игры """
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		# управляем частотой кадров
		self.clock = pygame.time.Clock()

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
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		# реагирует на нажатие клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True

		elif event.key == pygame.K_a:
			self.ship.image = self.ship.image_left
			self.ship.moving_left = True
		elif event.key == pygame.K_d:
			self.ship.image = self.ship.image_right
			self.ship.moving_right = True
		elif event.key == pygame.K_s:
			self.ship.image = self.ship.image_down
			self.ship.moving_down = True
		elif event.key == pygame.K_w:
			self.ship.image = self.ship.image_up
			self.ship.moving_up = True


		# закрытие окна при нажатии на q
		elif event.key == pygame.K_q:
			sys.exit()


	def _check_keyup_events(self, event):
		# реагирует на отпускание клавиш
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

		elif event.key == pygame.K_a:
			# self.ship.image = self.ship.image_up
			self.ship.moving_left = False
		elif event.key == pygame.K_d:
			# self.ship.image = self.ship.image_up
			self.ship.moving_right = False
		elif event.key == pygame.K_s:
			# self.ship.image = self.ship.image_up
			self.ship.moving_down = False
		elif event.key  == pygame.K_w:
			# self.ship.image = self.ship.image_up
			self.ship.moving_up = False


	def _update_screen(self):
		# Заполняем цветом фон, вызываем метод fill() с одним аргументом - цвет фона
			self.screen.fill(self.settings.bg_color)
			# рисуем корабль из модуля ship
			self.ship.blitme()
			# Отображение последнего отрисованного экрана
			pygame.display.flip()
			# частота кадров
			self.clock.tick(60)

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()