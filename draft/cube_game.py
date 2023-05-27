import pygame
import sys
from settings_pac import Settings
from pac import Pac
from ghost import Ghost
from bullet_pac import Bullet_Pac

class PacMan:
	"""Класс для управления ресурсами и поведением игры """
	def __init__(self):
		"""Инициализирует игру и создает игровые ресурсы"""
		pygame.init()
		self.settings = Settings()
		# экран в окне на основе параметров экрана из settings_pac
		# self.screen = pygame.display.set_mode((self.settings.screen_widht
		# 	, self.settings.screen_height))
		# полноэкранный режим
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption('PacMan')
		self.clock = pygame.time.Clock()
		self.pac = Pac(self)
		self.ghost = Ghost(self)

		# группировка снарядов
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Запуск основного кода игры"""
		while True:
			self._check_events()
			self.pac.update()
			self.bullets.update()
			self._update_bullets()
			self._update_screen()

	def _check_events(self):
		"""обрабатывает нажатия клавиш и события мыши"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			if event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_p:
			self.settings.bg_color = self.settings.bg_ping_color
		elif event.key == pygame.K_b:
			self.settings.bg_color = self.settings.bg_heavenly_color
		elif event.key == pygame.K_RIGHT:
			self.pac.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.pac.moving_left = True
		elif event.key == pygame.K_UP:
			self.pac.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.pac.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.pac.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.pac.moving_left = False
		elif event.key == pygame.K_UP:
			self.pac.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.pac.moving_down = False

	def _fire_bullet(self):
		"""Создание нового снаряда (экземпляр) и добавление его в группу"""
		if len(self.bullets) <= self.settings.bullet_allowed:
			new_bullet = Bullet_Pac(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Удаление старых снарядов"""
		for bullet in self.bullets.copy():
			if bullet.rect.right > self.settings.screen_width or bullet.rect.left <=  (self.pac.rect.left + 50):
				self.bullets.remove(bullet)

	def _update_screen(self):
		"""Обновляет изображения на экране и отображает новый экран"""
		self.screen.fill(self.settings.bg_color)
		self.pac.blitme()
		self.ghost.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()
		self.clock.tick(60)

if __name__ == '__main__':
	pac = PacMan()
	pac.run_game()