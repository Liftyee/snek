import pygame
from pygame.locals import *

print("loaded view")

class Button:
    def __init__(self, screen, x, y, width=None, height=None, text=None, color=(120, 200, 40)):
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
        self.wallColor = (200, 200, 200)

        self.dispW = displayWidth
        self.dispH = displayHeight

        pygame.init()
        self.screen = pygame.display.set_mode((displayWidth, displayHeight))
        pygame.display.set_caption("snek")

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
    
    def renderWalls(self, walls):
        for i in walls:
            tx = i[0]*self.gridScale
            ty = i[1]*self.gridScale
            pygame.draw.rect(self.screen, self.wallColor, (tx, ty, self.gridScale, self.gridScale))
    
    def renderScore(self, score):
        self.drawText("Score: " + str(score), 0, 0)

    def drawText(self, text, x, y):
        img1 = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(img1, (x, y))

    def gameOver(self, score, levelUp, level):

        self.clearScreen()
        self.drawText("Game Over!", 0, 0)
        self.drawText("Your score was: "+ str(score), 0, 40)

        restartBtn = Button(self.screen, 0, 80, 128, 32, "Retry")
        menuBtn = Button(self.screen, 0, 120, 128, 32, "Main menu")
        restartBtn.draw()
        menuBtn.draw()

        if levelUp:
            self.drawText("You leveled up to level " + str(level) + "!", 0, 160)

        if not self.update():
            return "exit"

        mousex, mousey = pygame.mouse.get_pos()
        if restartBtn.isPressed(mousex, mousey):
            return "restart"
        if menuBtn.isPressed(mousex, mousey):
            return "menu"
        return "GameOver"
    
    def mainMenu(self, level="N/A", highscore = "N/A"):
        self.clearScreen()
        self.screen.blit(pygame.image.load("snek.png"), (0, 0))

        startBtn = Button(self.screen, 0, self.dispH-128, 128, 32, "Start")
        resetBtn = Button(self.screen, 0, self.dispH-80, 128, 32, "Clear data")
        exitBtn = Button(self.screen, 0, self.dispH-32, 128, 32, "Exit")
    
        startBtn.draw()
        resetBtn.draw()
        exitBtn.draw()

        self.drawText("Level: " + str(level), 0, 200)
        self.drawText("Highscore: " + str(highscore), 0, 240)

        if not self.update():
            return "exit"

        mousex, mousey = pygame.mouse.get_pos()
        if startBtn.isPressed(mousex, mousey):
            return "restart"
        if resetBtn.isPressed(mousex, mousey):
            return "deldata"
        if exitBtn.isPressed(mousex, mousey):
            return "exit"
        return "menu"
    
    
    # add game over screen (retry, quit) 
    # add start screen menus, level up page (change speed for level)
    # add score on view

    #def renderScore(self, score):

    #def 