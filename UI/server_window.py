import tkinter as tk
from tkinter import scrolledtext
from Logic.server_logic import ServerLogic

class ServerWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("伺服器端")
        
        self.port_label = tk.Label(master, text="埠號:")
        self.port_label.pack()
        
        self.port_entry = tk.Entry(master)
        self.port_entry.pack()
        
        self.listen_button = tk.Button(master, text="開始聆聽", command=self.start_listening)
        self.listen_button.pack()
        
        self.chat_box = scrolledtext.ScrolledText(master, state='disabled')
        self.chat_box.pack()
        
        self.message_entry = tk.Entry(master)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(master, text="發送", command=self.send_message)
        self.send_button.pack()
        
        self.server_logic = ServerLogic(self)

    def start_listening(self):
        port = int(self.port_entry.get())
        self.server_logic.start_listening(port)

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state='disabled')

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.server_logic.send_message(message)
            self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    server_window = ServerWindow(root)
    root.mainloop()
