from random import randint # TEMPORARY
import src.view as view
import src.controller as controller


class SnakeGame:
	# class SnakeBody:
	# 	def __init__(self):
	# 		self.up = False
	# 		self.down = False
	# 		self.left = False
	# 		self.right = False
	# 		self.head = False

	def __init__(self, view=None):
		print("init snakegame")
		self.view = view

		# list of snake bodies
		self.snake = []
		self.maxLength = 5 # starting length 5, this changes
		
		self.boardX = 30 # board size
		self.boardY = 30
		self.score = 0

		self.FoodScoreInc = 100
		self.FoodLenInc = 3
		self.ExistScoreInc = 10

		self.food = []
		self.maxFood = 1
		self.maxFoodSpawnAttempts = 50

		self.level = 1
	
		# dirs dict maps word directions to change in (x, y) coordinates 
		self.dirs = {"up":(0,-1), "down":(0,1), "left":(-1,0), "right":(1,0)}
		self.dir = "right"

		self.initSnake(15, 15)
		# if view is given, every time status of game changes internally update the view
		# view.update(something): different updates for different changes
	
	def go_left(self):
		if self.dir != "right":
			self.dir = "left"
	
	def go_right(self):
		if self.dir != "left":
			self.dir = "right"
	
	def go_up(self): 
		if self.dir != "down":
			self.dir = "up"
	
	def go_down(self):
		if self.dir != "up":
			self.dir = "down"

	def initSnake(self, x, y, length=5):
		# adds some amount of units to the snake, initializes their coordinates in the list
		for i in range(x-length+1, x+1):
			self.snake.append([i, y])
	
	def getHeadPos(self):
		return (self.snake[-1][0], self.snake[-1][1])

	def spawnFood(self):
		valid = False
		attempts = 0
		while not valid and attempts < self.maxFoodSpawnAttempts:
			# generate a random position for the food
			### foodx, foody = controller.randpos(0, self.boardX, 0, self.boardY)
			# previous line doesn't work???  AttributeError: module 'src.controller' has no attribute 'randpos'
			foodx, foody = (randint(0, self.boardX), randint(0, self.boardY))
			
			# check if the position conflicts with snake body
			valid = True
			for i in self.snake:
				if i[0] == foodx and i[1] == foody:
					valid = False
					break
			
			# check if the position conflicts with existing food
			for i in self.food:
				if i[0] == foodx and i[1] == foody:
					valid = False
					break
			
			attempts += 1
		
		if valid:
			# the position is safe; add it
			self.food.append([foodx, foody])
		else:
			# we ran out of attempts
			print("Err: no positions to spawn food")

	def moveForward(self):

		if len(self.snake) >= self.maxLength:
			self.snake.pop(0)

		# get current x and y
		cx, cy = self.getHeadPos()

		# calculate changes to x and y
		dx = self.dirs[self.dir][0]
		dy = self.dirs[self.dir][1]

		self.snake.append([cx+dx, cy+dy])

	def checkGameOver(self):
		headX, headY = self.getHeadPos()

		# check for wall collide gameover
		if not 0<=headX<=self.boardX:
			return True
		if not 0<=headY<=self.boardY:
			return True

		# check for self collide gameover
		for n, i in enumerate(self.snake):
			if n == len(self.snake)-1:
				continue
			if i[0] == headX and i[1] == headY:
				#print("gameover due to self collision")
				return True
		
		return False

	def checkFood(self):
		headX, headY = self.getHeadPos()

		tmpFood = self.food[:]

		for n, i in enumerate(tmpFood):
			if i[0] == headX and i[1] == headY:
				self.food.pop(n)
				return True

		return False

	def doOutput(self):
		# check if a view is given
		if True:#self.view == None:
			print("Snake segments:", self.snake)
			print("Food locations:", self.food)
			print("Score:", self.score)
			print("Direction:", self.dir)
	

	def step(self):
		print("stepping...")
		# this function simulates the changing of the game, like an update() function
		# handle the updates from the controller
		# update the view 
		
		# check level 
		# update new food, show on view
		# change dir
		# move forward
		# check game over
		# check rewards (apple etc)
		# (whole update after this)
		# remove food if eaten
		
		# snake becomes longer? update list of snake bodies
		# update score and level of current game, game status (view.update(status) etc
		
		# Only Controller and View have pygame, this file should not need pygame - independent

		if len(self.food) < self.maxFood: 
			self.spawnFood()
		
		self.moveForward()

		if self.checkGameOver():
			print("snake is dead")
			return ("GameOver", self.score)

		if self.checkFood():
			self.maxLength += self.FoodLenInc
			self.score += self.FoodScoreInc


		self.score += self.ExistScoreInc # give some score for surviving

		# output the data
		self.doOutput()
		
		return None



