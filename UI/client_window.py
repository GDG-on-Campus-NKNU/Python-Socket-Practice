import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
import re
from tkinter import messagebox as mb
from Logic.client_logic import ClientLogic

class ClientWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("客戶端")
        self.master.configure(bg='#2C2C2C')

        custom_font = font.Font(family="Microsoft JhengHei", size=10)

        # Adding IP field
        self.ip_label = tk.Label(master, text="IP位址:", bg='#2C2C2C', fg='white', font=custom_font)
        self.ip_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.ip_entry = tk.Entry(master, bg='#424242', fg='white', font=custom_font, insertbackground='white')
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        self.port_label = tk.Label(master, text="埠號:", bg='#2C2C2C', fg='white', font=custom_font)
        self.port_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.port_entry = tk.Entry(master, bg='#424242', fg='white', font=custom_font, insertbackground='white')
        self.port_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        self.connect_button = tk.Button(master, text="連接", command=self.connect_to_server, bg='#5C5C5C', fg='white', font=custom_font)
        self.connect_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky='ew')

        self.chat_box = scrolledtext.ScrolledText(master, state='disabled', bg='#1E1E1E', fg='white', font=custom_font, insertbackground='white')
        self.chat_box.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        self.entry_prompt = tk.Label(master, text="輸入訊息:", bg='#2C2C2C', fg='white', font=custom_font)
        self.entry_prompt.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.message_entry = tk.Entry(master, bg='#424242', fg='white', font=custom_font, insertbackground='white')
        self.message_entry.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="發送", command=self.send_message, bg='#5C5C5C', fg='white', font=custom_font)
        self.send_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Configure grid to be resizable
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.protocol("WM_DELETE_WINDOW", self.on_window_closure)

        self.client_logic = ClientLogic(self)
        self.connection_state = False

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = int(self.port_entry.get() if self.port_entry.get().isdigit() else 0)

        if not ip or port == 0:
            self.display_message("錯誤: IP位址或埠號未提供或不合法\n")
            self.clear_fields()
            return

        # 簡單的IP格式驗證
        ip_pattern = re.compile("^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)){3}$")
        if not ip_pattern.match(ip) and not ip == "localhost":
            self.display_message("錯誤: IP位址格式不正確\n")
            self.clear_fields()
            return
        
        self.ip_entry.config(state='disabled')
        self.port_entry.config(state='disabled')

        self.connect_button.config(text="關閉連線", command=self.close_connection)

        self.client_logic.connect_to_server(ip, port)
        self.connection_state = True

    def close_connection(self):
        self.connection_state = False
        self.client_logic.close_connection()

        self.ip_entry.config(state='normal')
        self.port_entry.config(state='normal')

        self.connect_button.config(text="連接", command=self.connect_to_server)

    def display_message(self, message):
        try:
            self.chat_box.config(state='normal')
            self.chat_box.insert(tk.END, message + "\n")
            self.chat_box.config(state='disabled')
        except:
            pass
    
    def clear_fields(self):
        self.ip_entry.delete(0, tk.END)
        self.port_entry.delete(0, tk.END)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_logic.send_message(message)
            self.message_entry.delete(0, tk.END)

    def on_window_closure(self):
        self.master.after(0, self._show_closure_prompt)
        
    def _show_closure_prompt(self):
        result = mb.askyesno("確認", "確定要關閉對話窗口嗎？", parent=self.master)
        if result:
            self.close_connection()
            self.master.destroy()