class Controller:
	def __init__(self, game, view=None):
		self.screen = pygame.display.set_mode((width, height))
	def run(self):
		# while loop
		# listens to keyboard interrupts; calls functions for each key action
		# controls time steps and update rate of the view
		updateSpeed = 30 # FPS
		while True:
			
			self.screen.fill(0,0,0)
			
			# handle quit event
			for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
			
			keys = pygame.key.get_pressed()
			if keys[ord('a')]:
				game.go_left()
			if keys[ord('d')]:
				game.go_right()
			if keys[ord('w')]:
				game.go_up()
			if keys[ord('s')]:
				game.go_down()
			
			
			game.step()
			self.screen.flip()
			pygame.clock.tick(updateSpeed)
			
