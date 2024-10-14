import tkinter as tk
from tkinter import scrolledtext
from Logic.client_logic import ClientLogic

class ClientWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("客戶端")
        
        self.port_label = tk.Label(master, text="埠號:")
        self.port_label.pack()
        
        self.port_entry = tk.Entry(master)
        self.port_entry.pack()
        
        self.connect_button = tk.Button(master, text="連接", command=self.connect_to_server)
        self.connect_button.pack()
        
        self.chat_box = scrolledtext.ScrolledText(master, state='disabled')
        self.chat_box.pack()
        
        self.message_entry = tk.Entry(master)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(master, text="發送", command=self.send_message)
        self.send_button.pack()
        
        self.client_logic = ClientLogic(self)

    def connect_to_server(self):
        port = int(self.port_entry.get())
        self.client_logic.connect_to_server(port)

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state='disabled')

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_logic.send_message(message)
            self.message_entry.delete(0, tk.END)
