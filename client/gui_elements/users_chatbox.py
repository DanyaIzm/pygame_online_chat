import pygame

from gui_elements.base_gui_element import BaseGUIElement
from gui_manager import GUIManager

class UsersChatbox(BaseGUIElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, current_member_color, other_members_color, font_size, user_name):
        super().__init__(gui_manager, id, rect)
        self.font_size = font_size
        self.font = pygame.font.Font(self.gui_manager.font_path, self.font_size)
        self.member_color = current_member_color
        self.others_color = other_members_color
        self.current_member = user_name
        self.member_margin = 10
        self.members = []
    
    def add_users(self, *users):
        for user_name in users:
            self.members.append(user_name)

    def process_event(self, event):
        pass

    def update(self):
        pygame.draw.rect(self.gui_manager.screen, pygame.Color(140, 140, 140), self.rect)
        pygame.draw.rect(self.gui_manager.screen, pygame.Color(214, 222, 55), self.rect, 2)

        current_margin = self.member_margin

        for member in self.members:
            color = self.member_color if member == self.current_member else self.others_color
            rendered_member_text = self.font.render(member, False, color)

            self.gui_manager.screen.blit(rendered_member_text, (self.rect.x + 10, self.rect.y + current_margin))

            current_margin += self.font_size + self.member_margin
