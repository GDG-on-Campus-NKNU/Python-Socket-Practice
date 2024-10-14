import threading
import tkinter as tk
from UI.client_window import ClientWindow
from UI.server_window import ServerWindow

def run_client():
    client_root = tk.Tk()
    client_window = ClientWindow(client_root)
    client_root.mainloop()

def run_server():
    server_root = tk.Tk()
    server_window = ServerWindow(server_root)
    server_root.mainloop()

if __name__ == "__main__":
    client_thread = threading.Thread(target=run_client)
    server_thread = threading.Thread(target=run_server)

    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()
