class Settings():
	def __init__(self):
		# Инициализирует настройки игры
		# Параметры экрана
		self.screen_widht = 1600
		self.screen_height = 1200
		# Цвет фона  по схеме rgb, где (255, 0, 0) - красный, например
		# сероватый цвет фона:
		self.bg_color = (255, 192, 203)
		# управление скоростью передвижения (на полтора пикселя вместо одного)
		self.ship_speed = 10

		# параметры снаряда
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)