import pygame

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.users_chatbox import UsersChatbox
from settings import *


class UsersState(BaseGameState):
    def __init__(self, state_manager: GameStateManager, user_name, users):
        super().__init__(state_manager)
        self.gui_manager = GUIManager(self.state_manager.screen, self.state_manager.base_font_path)

        self.user_chatbox = UsersChatbox(
            self.gui_manager,
            'user_chatbox',
            pygame.rect.Rect(100, 100, SCREEN_WIDTH - 100 * 2, SCREEN_HEIGHT - 100 * 2),
            pygame.Color('yellow'),
            pygame.Color('coral'),
            font_size=20,
            user_name=user_name
        )

        self.user_chatbox.add_users(*users)
    
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_manager.pop_state()
        
        self.gui_manager.process_event(event)

    def update(self):
        self.gui_manager.update()

    def process_quit(self):
        pass
