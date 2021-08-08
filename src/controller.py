import pygame
from pygame.locals import *
from random import randint
import sys
print("loaded controller")
class Controller:

	def __init__(self, game, updateRate=5, view=None):
		self.game = game
		self.updateRate = updateRate
		self.keyboardCheckRate = 60

		if view == None:
			print("noview")
		self.view = view
		

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
		counter = 0
		while True:


			
			self.listenKeyboard()

			self.view.clearScreen()
			
			if counter >= self.keyboardCheckRate//self.updateRate:
				counter = 0
				status = self.game.step()
				if status != None:
					if status[0] == "GameOver":
						print("Game Over!")
						print("Score was", status[1])
						break
				
				if self.view != None:
					self.view.update()
			else:
				counter += 1
			
			



			clock.tick(self.keyboardCheckRate)
			
