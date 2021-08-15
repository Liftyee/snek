import pygame
from pygame.locals import *
from random import randint
import sys
print("loaded controller")
class Controller:

	def __init__(self, game, view=None):
		self.game = game
		self.updateRate = self.game.updateRate
		self.keyboardCheckRate = 60
		self.state = "menu"
		self.stateInfo = "" # stores information such as game over score, etc
		if view == None:
			print("noview")
		else:
			view.updateScale(game.boardX, game.boardY)
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

	def updateScale(self, x, y):
		self.view.updateScale(x, y)


	def run(self):
		clock = pygame.time.Clock()
		print("running")
		# while loop
		# listens to keyboard interrupts; calls functions for each key action
		# controls time steps and update rate of the view
		 # FPS
		counter = 0
		while True:
			if self.state == "run":
				try:
					self.listenKeyboard()
					
					if counter >= self.keyboardCheckRate//self.updateRate:
						counter = 0

						if self.view != None:
							self.view.clearScreen()

						status = self.game.step()
						if status != None:
							if status[0] == "GameOver":
								self.stateInfo = status[1]
								self.state = "GameOver"
								continue
						
						if self.view != None:
							print("drawing snek")
							print(status[0])
							self.view.renderSnake(status[0])
							self.view.renderFood(status[1])
							self.view.renderWalls(status[2])
							self.view.renderScore(self.game.score)
							if not self.view.update():
								self.state = "exit"
							
							
					else:
						counter += 1
					
					clock.tick(self.keyboardCheckRate)

				# something went wrong
				except Exception as ex:

					self.state = "error"
					self.stateInfo = ex

			# game over is happened
			elif self.state == "GameOver":
				self.state = self.view.gameOver(self.stateInfo, self.game.levelUp, self.game.level)
			
			elif self.state == "menu":
				self.state = self.view.mainMenu(self.game.level, self.game.highscore)
				
			elif self.state == "exit":
				self.game.saveData()
				return 0
			
			elif self.state == "restart":
				self.game.reset()
				self.state = "run"
				self.updateRate = self.game.updateRate

			elif self.state == "deldata":
				self.game.resetData()
				self.state = "menu"

			elif self.state == None:
				print("is none")
			else:
				print("An error occurred.")
				print(self.stateInfo)
				try: 
					self.view.clearScreen()
					self.view.drawText("Error! Check console for more info", 0, 0)
				except:
					pass
