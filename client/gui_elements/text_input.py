from gui_elements.base_gui_element import BaseGuiElement


class TextInput(BaseGuiElement):
    def __init__(self, id: str, color_active, color_passive):
        super().__init__(id)
        self.colors = (color_active, color_passive)

    def process_event(self, event):
        pass
    
    def update(self):
        pass
