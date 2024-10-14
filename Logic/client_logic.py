import socket
import threading
from datetime import datetime

class ClientLogic:
    def __init__(self, ui):
        self.ui = ui
        self.client_socket = None

    def connect_to_server(self, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', port))
        self.ui.display_message(f"<已建立與 127.0.0.1 的連線>")
        threading.Thread(target=self.receive_message).start()

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.ui.display_message(f"伺服器 {timestamp}: {message}")

    def send_message(self, message):
        if message and self.client_socket:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.ui.display_message(f"客戶端 {timestamp}: {message}")
            self.client_socket.send(message.encode())
