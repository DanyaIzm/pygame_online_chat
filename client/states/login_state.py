import pygame

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.text_label import TextLabel
from gui_elements.text_input import TextInput
from states.chat_state import ChatState
from settings import *


class LoginState(BaseGameState):
    def __init__(self, state_manager: GameStateManager):
        super().__init__(state_manager)

        # next state will be ChatState
        next_state = ChatState(self.state_manager)

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
            callback=next_state.set_self
            )
    
    def process_event(self, event):
        self.gui_manager.process_event(event)

    def update(self):
        self.gui_manager.update()
