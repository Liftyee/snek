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
        dImage = getattr(obj, "image")
        dRot = getattr(obj, "rotation")
        dScale = getattr(obj, "scale")


class Game:
    def __init__(self, width, height):
        self.screen = GameScreen(width, height)
        self.imgsPath = Path()

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


class Snake():
    def __init__(self, *args, **kwargs):
        self.direction
        self.speed
        self.growthRate
        self.length
        self.headX
        self.headY
    
        self.bodyUnits = []