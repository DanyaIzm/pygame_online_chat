import pygame
import sys

from settings import *
from gui_manager import GUIManager
from gui_elements.text_label import TextLabel
from gui_elements.text_input import TextInput


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font('assets/font.ttf', 20)

gui_manager = GUIManager(screen, font)

text_label = TextLabel(
    gui_manager,
    'text_label',
    pygame.Rect((SCREEN_WIDTH - 900) // 2, (SCREEN_HEIGHT - 60) // 2 - 200, 900, 60),
    text='Введите имя',
    color=pygame.Color('coral')
)

text_input = TextInput(
    gui_manager,
    'chat_input',
    pygame.Rect((SCREEN_WIDTH - 900) // 2, (SCREEN_HEIGHT - 60) // 2, 900, 60),
    pygame.Color('yellow'),
    pygame.Color('lightgray')
    )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        gui_manager.process_event(event)
    
    screen.fill((0, 0, 0))

    gui_manager.update()

    pygame.display.flip()

    clock.tick(FPS)
