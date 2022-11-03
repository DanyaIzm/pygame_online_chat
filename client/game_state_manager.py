class GameStateManager:
    def __init__(self, screen, font_path):
        self.screen = screen
        self.base_font_path = font_path
        self.current_states = []
    
    def set_state(self, state, exclusive=False):
        if exclusive:
            self.current_states = []
        self.current_states.append(state)
    
    def pop_state(self):
        state = self.current_states.pop()
        state.process_quit()
    
    def process_event(self, event):
        if self.current_states:
            self.current_states[-1].process_event(event)
        else:
            raise Exception('GameStateManager has no states. You should use set_state method to set state')
    
    def update(self):
        if self.current_states:
            for state in self.current_states:
                state.update()
        else:
            raise Exception('GameStateManager has no state. You should use set_state method to set state')
        
    def process_quit(self):
        for state in reversed(self.current_states):
            state.process_quit()
