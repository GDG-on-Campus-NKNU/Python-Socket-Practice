# -*- coding: utf-8 -*-

import socket
import threading

def handle_client(client_socket):
    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"\r客戶端: {message}\n伺服器: ", end='')
            except:
                print("\n客戶端已斷開連線")
                break

    threading.Thread(target=receive_messages).start()

    while True:
        message = input("伺服器: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # 修改為伺服器要監聽的 IP 和埠號
    server_socket.listen(1)

    print("伺服器正在聆聽...")

    client_socket, addr = server_socket.accept()
    print(f"已建立與 {addr[0]} 的連線")

    handle_client(client_socket)

if __name__ == "__main__":
    main()
