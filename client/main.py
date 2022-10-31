import pygame
import sys
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))

    pygame.display.flip()

    clock.tick(FPS)
