import pygame


print("loaded view")

# TODO: add display code...

class View:
    def __init__(self, displayWidth=640, displayHeight=640, gridX=30, gridY=30):
        # get the size each grid square should be in pixels
        self.gridScale = min(displayWidth//gridX, displayHeight//gridY)

        pygame.init()
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))
    
    def update(self):
        pygame.display.update()

    def clearScreen(self, r=0, g=0, b=0):
        self.screen.fill((r,g,b))

    def renderSnake(self, snake):
        for i in snake:
            tx = i[0]*self.gridScale
            ty = i[1]*self.gridScale
            pygame.draw.rect(self.screen, (255, 0, 0), (tx, ty, self.gridScale, self.gridScale))

    def renderFood(self, food):
        for i in food:
            tx = i[0]*self.gridScale
            ty = i[1]*self.gridScale
            pygame.draw.rect(self.screen, (0, 0, 255), (tx, ty, self.gridScale, self.gridScale))