import pygame


class GUIManager:
    def __init__(self, screen, font):
        self.screen = screen
        self.font: pygame.font.Font = font
        self.gui_elements = []
    
    def add_element(self, element):
        self.gui_elements.append(element)

    def process_event(self, event):
        """ Process current pygame event """
        for element in self.gui_elements:
            element.process_event(event)

    def update(self):
        """ Update gui elements each frame """
        for element in self.gui_elements:
            element.update()
