from random import randint # TEMPORARY
import pickle
import src.view as view
import src.controller as controller

class SnakeUnit:
	def __init__(self, x, y, dirs=[0,0,0,0]):
		self.dirs = dirs # up right down left
		self.pos = [x, y]
		self.head = False

class SnakeGame:


	def __init__(self, hasView=True, savefile="data.snk", databoardX=30, boardY=30):
		print("init snakegame")
		self.debug = False

		self.hasView = hasView
		
		self.boardX = 30 # board size
		self.boardY = 30

		self.FoodScoreInc = 500
		self.FoodLenInc = 3
		self.ExistScoreInc = 0

		self.maxFood = 1
		self.maxFoodSpawnAttempts = 50

		self.maxWalls = 0

		self.level = 1
		self.levelIncScore = 1000 # score increase for next level
		self.highscore = 0
		self.levelUp = False
		
		self.updateRate = 5
		self.baseUpdateRate = 5 # default move rate in FPS
		self.baseFood = self.maxFood
		self.baseWalls = self.maxWalls
		self.levelFPSInc = 1 # FPS increase per level
		self.levelFoodInc = 0.5 # food number increase per level
		self.levelWallInc = 0.5 # wall number increase per level

		# dirs dict maps word directions to change in (x, y) coordinates 
		self.dirs = {"up":(0,-1), "down":(0,1), "left":(-1,0), "right":(1,0)}
		self.dir = "right"

		self.savefile = savefile
		try:
			data = pickle.load(open(savefile, 'rb'))
			self.highscore = data["highscore"]
			self.level = data["level"]

		except Exception as e:
			print("error loading save:", e)
		self.reset()
		self.initSnake(15, 15)
		# if view is given, every time status of game changes internally update the view
		# view.update(something): different updates for different changes
	
	def reset(self):
		self.snake = []
		self.food = []
		self.walls = []
		self.initSnake(15, 15)
		self.score = 0
		self.maxLength = 5 # starting length 5, this changes
		self.levelUp = False
		self.maxFood = self.baseFood + (self.level*self.levelFoodInc)
		self.updateRate = self.baseUpdateRate + (self.level*self.levelFPSInc)
		self.maxWalls = self.baseWalls + (self.level*self.levelWallInc)

	def saveData(self):
		tempdata = {"highscore":self.highscore, "level":self.level}
		datafile = open(self.savefile, "wb")
		pickle.dump(tempdata, datafile)
		datafile.close()

	def resetData(self):
		self.highscore = 0
		self.level = 1

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
			self.snake.append(SnakeUnit(i, y))
		self.dir = "right"
	
	def getHeadPos(self):
		return (self.snake[-1].pos[0], self.snake[-1].pos[1])

	def spawnFood(self):
		valid = False
		attempts = 0
		while not valid and attempts < self.maxFoodSpawnAttempts:
			# generate a random position for the food
			foodx, foody = (randint(0, self.boardX), randint(0, self.boardY))
			
			# check if the position conflicts with snake body
			valid = True
			for i in self.snake:
				if i.pos[0] == foodx and i.pos[1] == foody:
					valid = False
					break
			
			# check if the position conflicts with existing food
			for i in self.food:
				if i[0] == foodx and i[1] == foody:
					valid = False
					break
			
			for i in self.walls:
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

	def spawnWall(self):
		valid = False
		attempts = 0

		# copy pasted code from spawning food
		while not valid and attempts < self.maxFoodSpawnAttempts:
			# generate a random position for the wall
			foodx, foody = (randint(0, self.boardX), randint(0, self.boardY))
			
			# check if the position conflicts with snake body
			valid = True
			for i in self.snake:
				if i.pos[0] == foodx and i.pos[1] == foody:
					valid = False
					break
			
			# check if the position conflicts with existing wall
			for i in self.food:
				if i[0] == foodx and i[1] == foody:
					valid = False
					break

			for i in self.walls:
				if i[0] == foodx and i[1] == foody:
					valid = False
					break
			
			attempts += 1
		
		if valid:
			# the position is safe; add it
			self.walls.append([foodx, foody])
		else:
			# we ran out of attempts
			print("Err: no positions to spawn wall")

	def calcdirindex(self, a, b):
		diff = (a[0]-b[0], a[1]-b[1])

		# based on (up, right, down, left)
		if diff == (0, 1):
			return 0
		if diff == (1, 0):
			return 3
		if diff == (0, -1):
			return 2
		if diff == (-1, 0):
			return 1
		
		print("what? two same coords sent to be calculated")
		return None

	def updateUnit(self, n, blind=False):
		unit = self.snake[n]
		unit.dirs = [0,0,0,0]
		if n >= 1 or blind:
			diridx = self.calcdirindex(unit.pos, self.snake[n-1].pos)
			if diridx:
				unit.dirs[diridx] = 1
		try:
			diridx = self.calcdirindex(unit.pos, self.snake[n+1].pos)
			if diridx:
				unit.dirs[diridx] = 1
		except IndexError:
			pass
		
	def recalcAllLinks(self):
		for i in range(len(self.snake)):
			self.updateUnit(i)

	def moveForward(self):

		if len(self.snake) >= self.maxLength:
			self.snake.pop(0)

		self.updateUnit(0)

		# get current x and y
		cx, cy = self.getHeadPos()

		# calculate changes to x and y
		dx = self.dirs[self.dir][0]
		dy = self.dirs[self.dir][1]

		self.snake.append(SnakeUnit(cx+dx, cy+dy))
		self.updateUnit(-1, True)
		self.updateUnit(-2, True)

	def checkGameOver(self):
		headX, headY = self.getHeadPos()
		# check for wall collide gameover
		if not 0<=headX<=self.boardX:
			print("gameover due to out of bounds")
			return True
		if not 0<=headY<=self.boardY:
			print("gameover due to out of bounds")
			return True

		# check for self collide gameover
		for n, i in enumerate(self.snake):
			if n == len(self.snake)-1:
				continue
			if i.pos[0] == headX and i.pos[1] == headY:
				print("gameover due to self collision")
				return True
		
		for i in self.walls:
				if i[0] == headX and i[1] == headY:
					print("gameover due to wall collision")
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
		if self.hasView == False or self.debug == True:
			print("Snake segments:", self.snake)
			print("Food locations:", self.food)
			print("Score:", self.score)
			print("Direction:", self.dir)

		if self.hasView == True:
			return (self.snake, self.food, self.walls)
	

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
		
		if len(self.walls) < self.maxWalls:
			self.spawnWall()

		self.moveForward()

		if self.checkFood():
			self.maxLength += self.FoodLenInc
			self.score += self.FoodScoreInc

		if self.checkGameOver():
			print("snake is dead")
			if self.score > self.highscore:
				self.highscore = self.score
			return ("GameOver", self.score)
		
		self.score += self.ExistScoreInc # give some score for surviving

		if self.score >= self.levelIncScore*self.level and not self.levelUp:
			self.level += 1
			self.levelUp = True

		print([i.dirs for i in self.snake])

		# output the data
		return self.doOutput()
		



