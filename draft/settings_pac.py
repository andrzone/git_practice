class Settings():
	"""Класс для хранения настроек игры"""
	def __init__(self):
		# настройки экрана
		self.screen_widht = 1200
		self.screen_height = 800
		self.bg_color = (127, 199, 255)
		self.bg_ping_color = (255, 192, 203)
		self.bg_heavenly_color = (127, 199, 255)
		# настройки героя
		self.pac_speed = 8.5
		# настройки выстрела
		self.bullet_speed = 5
		self.bullet_width = 5
		self.bullet_height = 5
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 5

		# circle = pygame.draw.circle(screen, (0, 0, 0), (100, 100), 15, 1)
