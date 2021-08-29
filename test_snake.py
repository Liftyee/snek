import unittest
from src.snake_game import SnakeGame

# make more testcases
class TestSnake(unittest.TestCase):

    def setUp(self):
        # setup code here
        print("nothing here")

    def test_godirection(self):
        game = SnakeGame(False)
        game.step()
        self.assertEqual(game.dir, "right")
        game.go_left()
        self.assertEqual(game.dir, "right")
        game.go_up()
        self.assertEqual(game.dir, "up")
        game.go_down()
        self.assertEqual(game.dir, "up")
        game.go_left()
        self.assertEqual(game.dir, "left")
        game.go_right()
        self.assertEqual(game.dir, "left")
        game.go_down()
        self.assertEqual(game.dir, "down")
        game.go_up()
        self.assertEqual(game.dir, "down")
        game.go_right()
        self.assertEqual(game.dir, "right")
    
    def test_deaths(self):
        game = SnakeGame(False)
        game.step()
        game.walls.append((16, 15))
        self.assertTrue(game.checkGameOver())  

if __name__ == '__main__':
    unittest.main()