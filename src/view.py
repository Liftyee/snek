import pygame
from pygame.locals import *

print("loaded view")

class Button:
    def __init__(self, screen, x, y, width=None, height=None, text=None, color=(200, 120, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.screen = screen
        self.font = pygame.font.SysFont('helvetica', int(self.height*0.8))
    
    def draw(self):
        # update self
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        if self.text != None:
            img1 = self.font.render(self.text, True, (255, 255, 255))
            self.screen.blit(img1, (self.x + self.height*0.1, self.y + self.height*0.1))

    def isPressed(self, mx, my):
        if pygame.mouse.get_pressed()[0]:
            if self.x <= mx <= self.x+self.width and self.y <= my <= self.y+self.height:
                return True
        return False

class View:

    def __init__(self, displayWidth=640, displayHeight=640):
        # get the size each grid square should be in pixels
        self.gridScale = 0

        self.snakeColor = (255, 0, 0)
        self.foodColor = (0, 255, 0)

        self.dispW = displayWidth
        self.dispH = displayHeight

        pygame.init()
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))

        # load a font (MIGHT NOT WORK ON LINUX)
        pygame.font.init()
        self.font = pygame.font.SysFont('helvetica', displayWidth//24)
    
    def handleQuit(self):
        # handle quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False
        return True

    def update(self):
        
        pygame.display.update()
        return self.handleQuit()

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
    
    def drawText(self, text, x, y):
        img1 = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(img1, (x, y))

    def gameOver(self, score):
        self.drawText("Game Over!", 0, 0)
        self.drawText("Your score was: "+ str(score), 0, 40)

        restartBtn = Button(self.screen, 0, 80, 128, 32, "Retry")
        menuBtn = Button(self.screen, 0, 120, 128, 32, "Main menu")
        restartBtn.draw()
        menuBtn.draw()
        if not self.update():
            return "stop"
        mousex, mousey = pygame.mouse.get_pos()
        if restartBtn.isPressed(mousex, mousey):
            return "restart"
        if menuBtn.isPressed(mousex, mousey):
            return "menu"
        return None
    # add game over screen (retry, quit) 
    # add start screen menus, level up page (change speed for level)
    # add score on view

    #def renderScore(self, score):

    #def 