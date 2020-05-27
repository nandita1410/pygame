import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Drawing")

#set up colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255, 0)
BLUE = (0,0, 255)
#set up the colors
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0), (291,106), (236,100), (250,150)))
pygame.draw.line(DISPLAYSURF, BLUE, (60,60), (120,60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120,60), (60,120) )
pygame.draw.line(DISPLAYSURF, BLUE, (60,120), (120,120),4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300,50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300,200, 40, 80),1)
pygame.draw.rect(DISPLAYSURF, RED , (200, 150, 100,50))

pixobj = pygame.PixelArray(DISPLAYSURF)
pixobj[380][280] = BLACK
pixobj[382][282] =  BLACK
pixobj[384][284] = BLACK
pixobj[386][286] = BLACK
pixobj[388][288] = BLACK


#run game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

