from gui_manager import GUIManager


class BaseGuiElement:
    def __init__(self, gui_manager: GUIManager, id: str, rect):
        self.id = id
        self.rect = rect
        self.gui_manager = gui_manager

        self.gui_manager.add_element(self)

    def process_event(self, event):
        raise NotImplementedError('This method must be overrided')
    
    def update(self):
        raise NotImplementedError('This method must be overrided')
