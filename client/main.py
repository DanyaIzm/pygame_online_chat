import pygame
import sys

from settings import *
from game_state_manager import GameStateManager
from states.login_state import LoginState


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font_path = 'assets/font.ttf'

state_manager = GameStateManager(screen, font_path)

# set initial game state
LoginState(state_manager).set_self()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        state_manager.process_event(event)
    
    screen.fill((0, 0, 0))

    state_manager.update()

    pygame.display.flip()

    clock.tick(FPS)
