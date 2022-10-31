import pygame

from gui_manager import GUIManager
from gui_elements.base_gui_element import BaseGUIElement


class TextInput(BaseGUIElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, color_active, color_passive, font_size, limit=30, callback=lambda: 0):
        super().__init__(gui_manager, id, rect)
        self.colors = (color_active, color_passive)
        self.color = self.colors[0]
        self.text = ''
        self.active = False
        self.error = False
        self.error_sound = pygame.mixer.Sound('assets/error_sound.wav')
        self.rect = rect
        self.font = pygame.font.Font(self.gui_manager.font_path, font_size)
        self.limit = limit
        self.callback = callback
    
    def _action(self) -> bool:
        if self.text:
            self.callback()
            return True
        else:
            return False

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # process click event
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            
        if not self.active:
            # if current text input is not active, we don't need to process events with it
            return

        if event.type == pygame.KEYDOWN:
            # process typing event
            self.error = False

            if event.key == pygame.K_RETURN:
                is_action_triggered = self._action()
                self.error = not is_action_triggered
                if self.error:
                    self.error_sound.play()

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if len(self.text) < self.limit:
                    self.text += event.unicode.strip()
                else:
                    self.error_sound.play()
                    self.error = True
    
    def update(self):
        if self.active:
            self.color = self.colors[0]
        else: 
            self.color = self.colors[1]

        if self.error:
            self.color = pygame.Color('red')

        rendered_text = self.font.render(self.text, False, self.color)

        pygame.draw.rect(self.gui_manager.screen, self.color, self.rect, 2)

        self.gui_manager.screen.blit(rendered_text, (self.rect.x + 10, self.rect.y + rendered_text.get_height() // 2))
