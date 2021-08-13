from src.snake_game import SnakeGame
from src.controller import Controller
from src.view import View


if __name__ == "__main__":
	view = View()
	snake_game = SnakeGame(True)
	controller = Controller(game=snake_game, view=view)
	controller.run()
