import pygame
from pathlib import Path

def loadImage(filePath, scale=None):
    img = pygame.image.load(filePath)
    if scale != None:
        pygame.transform.scale(img, (scale, scale))

class GameScreen:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    def drawObj(self, obj):
        drawX = getattr(obj, "posX")
        drawY = getattr(obj, "posY")
        dImage = getattr(obj, "image") # a pygame image object
        dRot = getattr(obj, "rotation")
        dScale = getattr(obj, "scale")

    def update(self):
        self.screen.clear()
        self.screen.fill(0,0,0)
        for event in pygame.event.get():
		    if event.type == QUIT:
			    pygame.quit()
			    sys.exit()
        


class Game:


    def __init__(self, width, height):
        self.screen = GameScreen(width, height)
        self.imgsPath = Path()

    def start(self, width, height):
        return Game(width, height)
    
    def reset():
        self.objects = []
        

    def update():
        for obj in self.objects:
            obj.update()
    
    def draw():
        for obj in self.objects:
            GameScreen.drawObj(obj)    
            

class GameObject(GameScreen):
    def __init__(self, *args, **kwargs):
        self.posX
        self.posY
        self.image
        self.rot
        self.scale

class SnakeGame(Game):
    self.snake = Snake()

    def go_up(self):
        return pygame.key.get_pressed()[ord('w')]
	
    def go_down(self):
        return pygame.key.get_pressed()[ord('s')]
        
    def go_left(self):
        return pygame.key.get_pressed()[ord('a')]
        
    def go_right(self):
        return pygame.key.get_pressed()[ord('d')]

class Snake():
    def __init__(self, *args, **kwargs):
        self.direction
        self.speed
        self.growthRate
        self.length
        self.headX
        self.headYwr
        self.bodyUnits = []