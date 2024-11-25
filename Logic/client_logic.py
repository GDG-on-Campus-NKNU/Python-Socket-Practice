import socket
import threading
from datetime import datetime
from tkinter import simpledialog

class ClientLogic:
    def __init__(self, ui):
        self.ui = ui
        self.client_socket = None

    def connect_to_server(self, ip, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, port))
            self.ui.display_message(f"<已建立與 {ip} 的連線>\n")
            threading.Thread(target=self.receive_message).start()
        except:
            self.ui.display_message("無法連線，因為目標電腦拒絕連線。\n")
            self.ui.close_connection()

    def receive_message(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode()
                if message:
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    self.ui.display_message(f"{timestamp} - 伺服器: {message}\n")
        except:
            self.ui.display_message(f"<連線已中斷: {'伺服器' if self.ui.connection_state else '客戶端'}已中斷一個現存的連線>\n")
            self.ui.close_connection()

    def send_message(self, message):
        if message and self.client_socket:
            timestamp = datetime.now().strftime('%H:%M:%S')
            self.ui.display_message(f"{timestamp} - 客戶端: {message}\n")
            self.client_socket.send(message.encode())

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
           