import 

class SnakeGame:
	def __init__(self, view=None):
		
		# if view is given, every time status of game changes internally update the view
		# view.update(something): different updates for different changes
		
	def step(self):
		
		# this function simulates the changing of the game, like an update() function
		# handle the updates from the controller
		# update the view 
		
		# check level 
		# change dir
		# move forward
		# check game over
		# check rewards (apple etc)
		# (whole update after this)
		# remove food if eaten
		# update new food, show on view
		# snake becomes longer? update list of snake bodies
		# update score and level of current game, game status (view.update(status) etc
		
		# Only Controller and View have pygame, this file should not need pygame - independent
