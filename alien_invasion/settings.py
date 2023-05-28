class Settings():
	def __init__(self):
		# Инициализирует настройки игры
		# Параметры экрана
		self.screen_widht = 1600
		self.screen_height = 1200
		# Цвет фона  по схеме rgb, где (255, 0, 0) - красный, например
		# сероватый цвет фона:
		self.bg_color = (255, 192, 203)
		# параметры корабля
		self.ship_speed = 10
		self.ship_limit = 3

		# параметры снаряда
		self.bullet_speed = 10
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 20

		# параметры пришельцев
		self.alien_speed = 2.0
		# fleep_drop_speed - величина снижения флота при достижении края
		self.fleep_drop_speed = 10
		# fleet_direction = 1 - движение вправо; -1 - влево
		self.fleet_direction = 1