import pygame
from pygame.locals import *
from random import randint
import sys
print("loaded controller")
class Controller:

	def __init__(self, game, updateRate=2, view=None):
		self.game = game
		self.updateRate = updateRate

		if view == None:
			print("noview")
		pygame.init()

		# TODO: MOVE TO VIEW
		self.screen = pygame.display.set_mode((640, 640))

	def randpos(self, startX, endX, startY, endY):
		return (randint(startX, endX), randint(startY, endY))

	def listenKeyboard(self):
					
		keys = pygame.key.get_pressed()
		if keys[ord('a')]:
			self.game.go_left()
		if keys[ord('d')]:
			self.game.go_right()
		if keys[ord('w')]:
			self.game.go_up()
		if keys[ord('s')]:
			self.game.go_down()


	def run(self):
		clock = pygame.time.Clock()
		print("running")
		# while loop
		# listens to keyboard interrupts; calls functions for each key action
		# controls time steps and update rate of the view
		 # FPS
		while True:
			
			# goes in view
			self.screen.fill((0,0,0))
			# ^

			# handle quit event
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					break
			
			self.listenKeyboard()

			
			
			status = self.game.step()
			if status != None:
				if status[0] == "GameOver":
					print("Game Over!")
					print("Score was", status[1])
					break
			
			# goes in view
			pygame.display.update()
			# ^

			# TODO: this makes the checking of keyboard only happen every update rate
			clock.tick(self.updateRate)
			
