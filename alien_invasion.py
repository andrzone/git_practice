import sys
import pygame

class AlienInvasion:
	"""Класс для управления ресурсами и поведением игры """
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1600, 1200))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		# Запуск основного кода игры

		while True:
			# Отслеживания событий клавы и мыши
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Отображение последнего отрисованного экрана
			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()