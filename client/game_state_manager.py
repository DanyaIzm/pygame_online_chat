class GameStateManager:
    def __init__(self, screen, font_path):
        self.screen = screen
        self.base_font_path = font_path
        self.current_state = None
    
    def set_state(self, state):
        self.current_state = state
    
    def process_event(self, event):
        if self.current_state:
            self.current_state.process_event(event)
        else:
            raise Exception('GameStateManager has no state. You should use set_state method to set state')
    
    def update(self):
        if self.current_state:
            self.current_state.update()
        else:
            raise Exception('GameStateManager has no state. You should use set_state method to set state')
