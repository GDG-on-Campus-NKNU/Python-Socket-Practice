import socket
import threading
from datetime import datetime

class ServerLogic:
    def __init__(self, ui):
        self.ui = ui
        self.server_socket = None
        self.client_socket = None

    def start_listening(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(1)
        self.ui.display_message("伺服器正在聆聽...")
        threading.Thread(target=self.accept_connection).start()

    def accept_connection(self):
        self.client_socket, addr = self.server_socket.accept()
        self.ui.display_message(f"<已建立與 {addr[0]} 的連線>")
        threading.Thread(target=self.receive_message).start()

    def receive_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if message:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.ui.display_message(f"客戶端 {timestamp}: {message}")

    def send_message(self, message):
        if message and self.client_socket:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.ui.display_message(f"伺服器 {timestamp}: {message}")
            self.client_socket.send(message.encode())
