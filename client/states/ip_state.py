import pygame

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.text_input import TextInput
from gui_elements.text_label import TextLabel
from states.login_state import LoginState
from settings import *


class IPState(BaseGameState):
    def __init__(self, state_manager: GameStateManager):
        super().__init__(state_manager)

        def set_next_state(ip_address):
            next_state = LoginState(self.state_manager, ip_address.strip())
            next_state.set_self()

        self.gui_manager = GUIManager(self.state_manager.screen, self.state_manager.base_font_path)

        self.text_label = TextLabel(
            self.gui_manager,
            'text_label',
            pygame.Rect((SCREEN_WIDTH - 900) // 2, (SCREEN_HEIGHT - 60) // 2 - 100, 900, 60),
            text='Введите IP адрес',
            color=pygame.Color('limegreen'),
            font_size=60
        )

        self.text_input = TextInput(
            self.gui_manager,
            'ip_input',
            pygame.Rect((SCREEN_WIDTH - 900) // 2, (SCREEN_HEIGHT - 60) // 2, 900, 60),
            pygame.Color('yellow'),
            pygame.Color('lightgray'),
            font_size=20,
            callback=set_next_state
            )

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.text_input.active = True
        self.gui_manager.process_event(event)

    def update(self):
        self.gui_manager.update()
    
    def process_quit(self):
        pass
