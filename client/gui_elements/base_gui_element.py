class BaseGuiElement:
    def __init__(self, id: str):
        self.id = id

    def process_event(self, event):
        raise NotImplementedError('This method must be overrided')
    
    def update(self):
        raise NotImplementedError('This method must be overrided')
