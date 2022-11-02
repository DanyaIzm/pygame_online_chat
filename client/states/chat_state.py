import pygame
import socket
import json

from states.base_game_state import BaseGameState
from game_state_manager import GameStateManager
from gui_manager import GUIManager
from gui_elements.chat_box import ChatBox
from gui_elements.text_input import TextInput
from settings import *


class ChatState(BaseGameState):
    def __init__(self, state_manager: GameStateManager, user_name, ip_address):
        super().__init__(state_manager)

        self.gui_manager = GUIManager(self.state_manager.screen, self.state_manager.base_font_path)

        self.member_name = user_name
        self.socket = None

        self.chat_box = ChatBox(
            self.gui_manager,
            'chat_box',
            pygame.Rect(10, 10, SCREEN_WIDTH - 10 * 2, SCREEN_HEIGHT - 90),
            pygame.Color('yellow'),
            pygame.Color('coral'),
            pygame.Color(224, 224, 224),
            font_size=20,
            user_name=self.member_name
        )

        self.text_input = TextInput(
            self.gui_manager,
            'chat_text_input',
            pygame.Rect(10, SCREEN_HEIGHT - 70, SCREEN_WIDTH - 10 * 2, 60),
            pygame.Color('yellow'),
            pygame.Color('lightgray'),
            font_size=20,
            limit=50,
            callback=self.send_message
        )

        self.establish_connection(ip_address)
    
    def establish_connection(self, ip_address):
        port = 25560

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip_address, port))
        self.socket.setblocking(False)
        self.socket.sendall(self.member_name.encode())

    def receive_message(self):
        try:
            data = self.socket.recv(1024).decode()
            data = json.loads(data)

            if data['method'] == 'QUIT':
                data['message'] = f'Пользователь {data["username"]} отключился'
                data['username'] = None
            elif data['method'] == 'CONNECT':
                data['message'] = f'Пользователь {data["username"]} присоединился'
                data['username'] = None

            self.chat_box.add_message(data['username'], data['message'])
        except:
            pass

    def send_message(self, message):
        data = self.make_message(message)
        self.socket.sendall(data)

    def make_message(self, message=None, method='MESSAGE'):
        data = {
            'method': method,
            'username': self.member_name,
            'message': message
        }

        return json.dumps(data).encode()
    
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                self.text_input.active = True
        self.gui_manager.process_event(event)

    def update(self):
        self.receive_message()
        self.gui_manager.update()

    def process_quit(self):
        self.socket.sendall(self.make_message(method='QUIT'))
        self.socket.close()
