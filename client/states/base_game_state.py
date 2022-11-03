from game_state_manager import GameStateManager


class BaseGameState:
    def __init__(self, state_manager: GameStateManager):
        self.state_manager = state_manager
    
    def set_self(self, exclusive=False, *args, **kwargs):
        self.state_manager.set_state(self, exclusive)

    def process_event(self, event):
        raise NotImplementedError('This method must be overrided')
    
    def update(self):
        raise NotImplementedError('This method must be overrided')
    
    def process_quit(self):
        raise NotImplementedError('This method must be overrided')
