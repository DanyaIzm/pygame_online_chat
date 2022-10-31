import pygame

from gui_elements.base_gui_element import BaseGUIElement
from gui_manager import GUIManager


class ChatBox(BaseGUIElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, current_member_color, other_members_color, message_color, font_size, user_name):
        super().__init__(gui_manager, id, rect)
        self.font_size = font_size
        self.font = pygame.font.Font(self.gui_manager.font_path, self.font_size)
        self.member_color = current_member_color
        self.others_color = other_members_color,
        self.message_color = message_color
        self.member_name = user_name
        self.message_margin = 10
        self.message_limit = (self.rect.height - self.message_margin) // (self.font_size + self.message_margin)
        self.messages = []
    
    def add_message(self, message):
        self.messages.append((self.member_name, message))

        if len(self.messages) > self.message_limit:
            self.messages.pop(0)
    
    def process_event(self, event):
        pass

    def update(self):
        pygame.draw.rect(self.gui_manager.screen, pygame.Color('lightgray'), self.rect, 2)

        current_margin = self.message_margin

        for message in self.messages:
            user_color = self.member_color if message[0] == self.member_name else self.others_color

            current_user = self.font.render(message[0] + ': ', False, user_color)
            current_message = self.font.render(message[1], False, self.message_color)

            self.gui_manager.screen.blit(current_user, (self.rect.x + 10, self.rect.y + current_margin))
            self.gui_manager.screen.blit(current_message, (self.rect.x + 10 + current_user.get_width(), self.rect.y + current_margin))

            current_margin += self.font_size + self.message_margin
