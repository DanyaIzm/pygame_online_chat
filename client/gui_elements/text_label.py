import pygame

from gui_manager import GUIManager
from gui_elements.base_gui_element import BaseGUIElement


class TextLabel(BaseGUIElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, text, color, font_size):
        super().__init__(gui_manager, id, rect)

        font = pygame.font.Font(self.gui_manager.font_path, font_size)
        self._rendered_text = font.render(text, False, color)
    
    def process_event(self, event):
        pass

    def update(self):
        self.gui_manager.screen.blit(
            self._rendered_text,
            (self.rect.x + self._rendered_text.get_width() // 2, self.rect.y),
            )
