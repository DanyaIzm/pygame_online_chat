import pygame

from gui_manager import GUIManager
from gui_elements.base_gui_element import BaseGuiElement


class TextInput(BaseGuiElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, color_active, color_passive):
        super().__init__(gui_manager, id, rect)
        self.colors = (color_active, color_passive)
        self.color = self.colors[0]
        self.text = ''
        self.active = False

    def process_event(self, event):
        pass
    
    def update(self):
        if self.active:
            self.color = self.colors[0]
        else: 
            self.color = self.colors[1]

        rendered_text = self.gui_manager.font.render(self.text, False, self.color)

        pygame.draw.rect(self.gui_manager.screen, self.color, self.rect, 2)

        self.gui_manager.screen.blit(rendered_text, (self.rect.x + 10, self.rect.y + 10))
