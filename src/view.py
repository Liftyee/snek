import pygame
from pygame.locals import *

print("loaded view")

# TODO: add display code...

class View:
    def __init__(self, displayWidth=320, displayHeight=640):
        # get the size each grid square should be in pixels
        self.gridScale = 0

        self.snakeColor = (255, 0, 0)
        self.foodColor = (0, 255, 0)

        self.dispW = displayWidth
        self.dispH = displayHeight

        pygame.init()
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))
    
    def update(self):
        # handle quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
        pygame.display.update()
        return True

    def clearScreen(self, r=0, g=0, b=0):
        self.screen.fill((r,g,b))

    def updateScale(self, gridX, gridY):
        self.gridScale = min(self.dispW//gridX, self.dispH//gridY)


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

    # add game over screen (retry, quit) 
    # add start screen, level up page (change speed for level)
    # add score on view

    #def renderScore(self, score):

    #def 