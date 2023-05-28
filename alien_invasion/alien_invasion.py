import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class AlienInvasion:
	"""Класс для управления ресурсами и поведением игры """
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		# созлание экземпляра для хранения игровой статистики
		self.stats = GameStats(self)
		self.ship = Ship(self)
		# управляем частотой кадров
		self.clock = pygame.time.Clock()
		# Группа для хранения и прорисовки всех летящих снарядов
		# Список с расширенным функционалом
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		# Запуск основного кода игры
		while True:
			self._check_events()
			# При каждом проходе цикла обновляется позиция корабля
			if self.stats.game_active:
				self.ship.update()
				# При каждом проходе обновляется позиция снарядов
				self._update_bullets()
				self._update_aliens()
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

		# пробел для выстрела снарядов
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


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

	def _fire_bullet(self):
		"""Создание нового снаряда и включение его в группу bullets"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_fleet(self):
		"""Создание пришельца и включение его в новый флот"""
		alien = Alien(self)
		# вычисление количества пришельцев в ряду
		# интервал между прищельцами равен ширине пришельца
		alien_width = alien.rect.width
		# интервал между прищельцами по рядам равен высоте пришельца
		alien_height = alien.rect.height
		# высота корабля
		ship_height = self.ship.rect.height
		# вычислим доступное горизонтальное пространство
		available_spase_x = int(self.settings.screen_width - (1.5 * alien_width))
		# количество доступных прищельцев на экране
		number_aliens_x  = int(available_spase_x // (alien_width * 2))

		# вычислим доступное вертикальное пространство
		available_spase_y = self.settings.screen_height - 3 * alien_height - ship_height
		# количество доступных рядов на экране
		number_rows  = available_spase_y // (alien_height * 2)

		# создание первого ряда пришельца
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._creat_alien(alien_number, row_number)

	def _creat_alien(self, alien_number, row_number):
		# создание первого прищельца и размещение его в ряду
		alien = Alien(self)
		alien.x = int(alien.rect.width + 2 * alien.rect.width * alien_number)
		alien.rect.x = alien.x
		alien.rect.y = int(alien.rect.height + 1.8 * alien.rect.height * row_number)
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Реагирует на достижение прищельцем края экрана"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Опускает весь флот и меняет его направление"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleep_drop_speed
		self.settings.fleet_direction *= -1


	def _update_bullets(self):
		"""Обновляет позиции снарядов и уничтожает старые"""
		self.bullets.update()
		# удаление снарядов, вышедших за край экрана
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		# проверка попаданий в пришельцев
		# при обнаружении попадания - удалить пришельца и снаряд
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if not self.aliens:
			# уничтожение существующих снарядов и создание нового флота
			self.bullets.empty()
			self._create_fleet()

	def _check_ship_aliens_collisions(self):
		"""Проверка коллизий корабль - пришельцы"""
		# коллизия: спрайт - группа
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

	def _check_aliens_bottom(self):
		"""Проверка, добрались ли пришельцы до нижней части экрана"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# происходит то же, что при столкновении с кораблем
				self._ship_hit()
				break

	def _ship_hit(self):
		"""Обрабатывает столкновение корабля с пришельцем"""
		# Уменьшение ship_left
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			# очистка списков пришельцев и снарядов
			self.aliens.empty()
			self.bullets.empty()
			# создание нового флота и размещение корабля
			self._create_fleet()
			self.ship.center_ship()
			# пауза
			sleep(0.5)
		else:
			self.stats.game_active = False

	def _update_aliens(self):
		"""Обновляет позиции всех пришельцев во флоте"""
		self._check_fleet_edges()
		self._check_ship_aliens_collisions()
		self._check_aliens_bottom()
		self.aliens.update()

	def _update_screen(self):
		# Заполняем цветом фон, вызываем метод fill() с одним аргументом - цвет фона
			self.screen.fill(self.settings.bg_color)
			# рисуем корабль из модуля ship
			self.ship.blitme()
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			self.aliens.draw(self.screen)
			# Отображение последнего отрисованного экрана
			pygame.display.flip()
			# частота кадров
			self.clock.tick(240)

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()