import pygame

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.chat_box import ChatBox
from gui_elements.text_input import TextInput
from settings import *


class ChatState(BaseGameState):
    def __init__(self, state_manager: GameStateManager, user_name):
        super().__init__(state_manager)

        self.gui_manager = GUIManager(self.state_manager.screen, self.state_manager.base_font_path)

        self.member_name = user_name

        self.chat_box = ChatBox(
            self.gui_manager,
            'chat_box',
            pygame.Rect(10, 10, SCREEN_WIDTH - 10 * 2, SCREEN_HEIGHT - 90),
            pygame.Color('yellow'),
            pygame.Color('coral'),
            pygame.Color('blue'),
            font_size=20,
            user_name=self.member_name
        )

        self.text_input = TextInput(
            self.gui_manager,
            'chat_text_input',
            pygame.Rect(10, SCREEN_HEIGHT - 70, SCREEN_WIDTH - 10 * 2, 60),
            pygame.Color('yellow'),
            pygame.Color('lightgray'),
            font_size=20,
            limit=50,
            callback=self.chat_box.add_message
        )

        self.member_name = None
    
    def process_event(self, event):
        self.gui_manager.process_event(event)

    def update(self):
        self.gui_manager.update()

    def process_quit(self):
        pass
