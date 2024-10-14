# -*- coding: utf-8 -*-

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\r伺服器: {message}\n你: ", end='')
        except:
            print("\n與伺服器的連線已中斷")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)  # 修改為伺服器的 IP 和埠號
    client_socket.connect(server_address)

    print("已連接到伺服器")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input("你: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()