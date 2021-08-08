import pygame
from pygame.locals import *

print("loaded view")

# TODO: add display code...

class View:
    def __init__(self, displayWidth=640, displayHeight=640, gridX=30, gridY=30):
        # get the size each grid square should be in pixels
        self.gridScale = min(displayWidth//gridX, displayHeight//gridY)

        self.snakeColor = (255, 0, 0)
        self.foodColor = (0, 255, 0)

        pygame.init()
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))
    
    def update(self):
        # handle quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        pygame.display.update()

    def clearScreen(self, r=0, g=0, b=0):
        self.screen.fill((r,g,b))

    def renderSnake(self, snake):
        for i in snake:
            tx = i[0]*self.gridScale
            ty = i[1]*self.gridScale
            pygame.draw.rect(self.screen, self.snakeColor, (tx, ty, self.gridScale, self.gridScale))

    def renderFood(self, food):
        for i in food:
            tx = i[0]*self.gridScale
            ty = i[1]*self.gridScale
            pygame.draw.rect(self.screen, self.foodColor, (tx, ty, self.gridScale, self.gridScale))