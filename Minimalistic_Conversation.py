import tkinter as tk
from UI.client_window import ClientWindow
from UI.server_window import ServerWindow

def run_application():
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗

    # 創建兩個獨立的窗口
    client_root = tk.Toplevel(root)
    client_root.title("客戶端")
    ClientWindow(client_root)

    server_root = tk.Toplevel(root)
    server_root.title("伺服器端")
    ServerWindow(server_root)

    root.mainloop()

if __name__ == "__main__":
    run_application()
