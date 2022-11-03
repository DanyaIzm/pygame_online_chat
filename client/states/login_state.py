import pygame

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.text_label import TextLabel
from gui_elements.text_input import TextInput
from states.chat_state import ChatState
from settings import *


class LoginState(BaseGameState):
    def __init__(self, state_manager: GameStateManager, ip_address):
        super().__init__(state_manager)

        # next state will be ChatState
        def set_next_state(user_name):
            next_state = ChatState(self.state_manager, user_name, ip_address)
            next_state.set_self(exclusive=True)

        self.gui_manager = GUIManager(self.state_manager.screen, self.state_manager.base_font_path)

        self.text_label = TextLabel(
            self.gui_manager,
            'text_label',
            pygame.Rect((SCREEN_WIDTH - 900) // 2, (SCREEN_HEIGHT - 60) // 2 - 100, 900, 60),
            text='Введите имя',
            color=pygame.Color('coral'),
            font_size=60
        )

        self.text_input = TextInput(
            self.gui_manager,
            'chat_input',
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
