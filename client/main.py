import pygame
import sys

from settings import *
from game_state_manager import GameStateManager
from states.ip_state import IPState


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font_path = 'assets/font.ttf'

state_manager = GameStateManager(screen, font_path)

# set initial game state
IPState(state_manager).set_self()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state_manager.process_quit()
            pygame.quit()
            sys.exit()
        
        state_manager.process_event(event)
    
    screen.fill((0, 0, 0))

    state_manager.update()

    pygame.display.flip()

    clock.tick(FPS)
