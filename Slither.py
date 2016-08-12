import pygame
import random

pygame.init()

#red green blue
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

appleThickness = 25
block_size = 15.0
FPS = 30
font = pygame.font.SysFont(None, 25)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])

def msg2screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/3.5, display_height/2])

def score(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 10])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    points = 0
    snakeList=[]
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width- appleThickness)/block_size)*block_size
    randAppleY = round(random.randrange(0, display_height- appleThickness)/block_size)*block_size

    while not gameExit:

        while gameOver == True :
            gameDisplay.fill(white)
            msg2screen("Game Over,press C to continue or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        score(str(points), green)
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,appleThickness,appleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        snake(block_size, snakeList)
        pygame.display.update()

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX = round(random.randrange(0, display_width - appleThickness) / block_size) * block_size
                randAppleY = round(random.randrange(0, display_height - appleThickness) / block_size) * block_size
                snakeLength += 1
                points += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX = round(random.randrange(0, display_width - appleThickness) / block_size) * block_size
                randAppleY = round(random.randrange(0, display_height - appleThickness) / block_size) * block_size
                snakeLength += 1
                points += 1


        if lead_x >= display_width or lead_x <= -block_size or lead_y >= display_height or lead_y <= -block_size:
            gameOver = True


        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()