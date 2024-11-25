import socket
import threading
from datetime import datetime

class ServerLogic:
    def __init__(self, ui):
        self.ui = ui
        self.server_socket = None
        self.client_socket = None

    def start_listening(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(1)
        self.ui.display_message("伺服器正在聆聽...\n")
        threading.Thread(target=self.accept_connection).start()

    def accept_connection(self):
        try:
            self.client_socket, addr = self.server_socket.accept()
            self.ui.display_message(f"<已建立與 {addr[0]} 的連線>\n")
            threading.Thread(target=self.receive_message).start()
        except:
            self.ui.display_message(f"<連線已中斷: {'伺服器' if not self.ui.connection_state else '客戶端'}已中斷一個現存的連線>\n")
            self.ui.close_connection()

    def receive_message(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if message:
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    self.ui.display_message(f"{timestamp} - 客戶端: {message}\n")
        except:
            self.ui.display_message(f"<連線已中斷: {'伺服器' if not self.ui.connection_state else '客戶端'}已中斷一個現存的連線>\n")
            self.ui.close_connection()

    def send_message(self, message):
        if message and self.client_socket:
            timestamp = datetime.now().strftime('%H:%M:%S')
            self.ui.display_message(f"{timestamp} - 伺服器: {message}\n")
            self.client_socket.send(message.encode())

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
