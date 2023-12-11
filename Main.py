import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FRAME_RATE = 100
clock = pygame.time.Clock()

xGround = 0
xBg = 0
counter = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (600, 704))
ground = pygame.image.load('ground.png')
ground = pygame.transform.scale(ground, (1296, 144))

run = True
while run:

    # Clock + ScreenFill:
    clock.tick(FRAME_RATE)
    screen.fill((0, 0, 0))

    # Background:
    screen.blit(bg, (xBg, 0))
    screen.blit(bg, (xBg + 600, 0))
    screen.blit(bg, (xBg + 1200, 0))

    if xBg == - 600:
        xBg = 0
    xBg -= 0.25

    # Ground:
    screen.blit(ground, (xGround, 704))
    screen.blit(ground, (xGround + 1296, 704))
    if xGround < -1296:
        xGround = 0
    xGround -= 2

    # Quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
