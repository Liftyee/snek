if __name__ == "main":
	view = View()
	snake_game = SnakeGame(view=view)
	controller = Controller(game=snake_game, view=view)
	controller.run()
