# -*- coding: utf-8 -*-

import socket
import threading

def handle_server(client_socket):
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"\r伺服器: {message}\n你: ", end='')
            except:
                print("\n與伺服器的連線已中斷")
                break

    threading.Thread(target=receive_messages).start()

    while True:
        message = input("你: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

    client_socket.close()

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)  # 修改為伺服器的 IP 和埠號
    client_socket.connect(server_address)

    print("已連接到伺服器")

    handle_server(client_socket)

if __name__ == "__main__":
    main()