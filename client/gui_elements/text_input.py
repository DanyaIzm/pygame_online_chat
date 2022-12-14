import pygame

from gui_elements.base_gui_element import BaseGUIElement
from gui_manager import GUIManager


class TextInput(BaseGUIElement):
    def __init__(self, gui_manager: GUIManager, id: str, rect, color_active, color_passive, font_size, limit=30, callback=lambda x: 0):
        super().__init__(gui_manager, id, rect)
        self.colors = (color_active, color_passive)
        self.color = self.colors[0]
        self.text = ''
        self.active = False
        self.error = False
        self.error_sound = pygame.mixer.Sound('assets/error_sound.wav')
        self.font = pygame.font.Font(self.gui_manager.font_path, font_size)
        self.limit = limit
        self.callback = callback

        self.is_backspace_hold = False
        self.backspace_start_delay = 20
        self.backspace_delay = 4
        self.backspace_counter = 0

        self.is_text_selected = False
    
    def _action(self) -> bool:
        if self.text.strip():
            self.callback(self.text.strip())
            self.text = ''
            return True
        else:
            return False

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # process click event
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.is_text_selected = False
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
                return
            
            # delete all text if it was selected
            if self.is_text_selected:
                    if not event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        self.text = ''
                    self.is_text_selected = False

            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.is_backspace_hold = True
            else:
                if len(self.text) < self.limit:
                    self.text += event.unicode
                else:
                    self.error_sound.play()
                    self.error = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                self.backspace_counter = 0
                self.is_backspace_hold = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LCTRL] and keys[pygame.K_a]:
            self.is_text_selected = True
            # this is needed to delete ^a symbol
            self.text = self.text[:-1]
    
    def update(self):
        if self.is_backspace_hold:
            self.backspace_counter += 1
            if self.backspace_counter == self.backspace_delay + self.backspace_start_delay:
                self.backspace_counter = self.backspace_start_delay
                self.text = self.text[:-1]

        if self.active:
            self.color = self.colors[0]
        else: 
            self.color = self.colors[1]

        if self.error:
            self.color = pygame.Color('red')
        
        if self.is_text_selected:
            text_background = pygame.Color('blue')
        else:
            text_background = None

        rendered_text = self.font.render(self.text, False, self.color, text_background)

        pygame.draw.rect(self.gui_manager.screen, self.color, self.rect, 2)

        self.gui_manager.screen.blit(rendered_text, (self.rect.x + 10, self.rect.y + rendered_text.get_height() // 2))
