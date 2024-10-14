# Minimalistic Conversation

這是一個簡單的聊天應用程式範例，包含客戶端和伺服器端的界面和邏輯分離。使用 Tkinter 作為 GUI 庫，並使用 socket 進行網路通信。

## 專案結構
```graphql
Minimalistic Conversation/ 
│ 
├── Logic/ 
│   ├── client_logic.py 
│   └── server_logic.py 
│ 
├── UI/ 
│   ├── client_window.py 
│   └── server_window.py 
│ 
├── Minimalistic_Conversation.py 
└── README.md
```
## 使用說明

### 1. 安裝依賴

確保你已經安裝了 Python 3.10 版本，並且安裝了 Tkinter 庫。Tkinter 通常隨 Python 一起安裝。

### 2. 運行應用程式

在專案根目錄下運行以下命令來啟動應用程式：

```bash
python Minimalistic_Conversation.py
```


這將會同時啟動客戶端和伺服器端的視窗。

### 3. 使用應用程式

1. **伺服器端**：
    - 在 "埠號" 輸入框中輸入要監聽的埠號（例如：12345）。
    - 點擊 "開始聆聽" 按鈕開始監聽客戶端的連接。
    - 在訊息輸入框中輸入訊息並按下 "發送" 按鈕或按下 Enter 鍵來發送訊息。

2. **客戶端**：
    - 在 "埠號" 輸入框中輸入伺服器的埠號（例如：12345）。
    - 點擊 "連接" 按鈕連接到伺服器。
    - 在訊息輸入框中輸入訊息並按下 "發送" 按鈕或按下 Enter 鍵來發送訊息。

### 注意事項

- 確保伺服器端和客戶端使用相同的埠號進行通信。
- 伺服器端需要先啟動並開始監聽，然後客戶端才能連接到伺服器。
