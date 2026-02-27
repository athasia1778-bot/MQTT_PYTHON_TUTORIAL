# MQTT Python 教程

這是一個簡單的 MQTT（消息佇列遙測傳輸）Python 實現教程項目，演示了發佈者-訂閱者模式的基本用法。

## 項目描述

本項目包含一個完整的 MQTT 應用示例，包括：
- **發佈者（Publisher）**：自動連接到 MQTT 代理並定期發送消息
- **訂閱者（Receiver）**：連接到代理並接收發佈者發送的消息
- **啟動器（Launcher）**：在獨立窗口中同時運行發佈者和訂閱者

## 文件結構

```
.
├── main.py              # 啟動器 - 打開發佈者和接收者的獨立窗口
├── publisher.py         # MQTT 發佈者 - 自動發送消息
├── receiver.py          # MQTT 接收者 - 接收消息
├── run_publisher.bat    # Windows 發佈者運行腳本
├── run_receiver.bat     # Windows 接收者運行腳本
└── README.md           # 本文件
```

## 系統需求

- Python 3.7 或更高版本
- paho-mqtt 庫

## 安裝

1. 克隆或下載此項目

2. 安裝依賴包：
```bash
pip install paho-mqtt
```

## 使用方法

### 方法一：使用啟動器（推薦）

在項目根目錄運行：
```bash
python main.py
```

這將自動打開兩個新窗口：
- 一個運行接收者
- 一個運行發佈者

### 方法二：分別運行

**運行接收者：**
```bash
python receiver.py
```

**在另一個終端運行發佈者：**
```bash
python publisher.py
```

### 方法三：Windows 批處理文件

直接雙擊運行：
- `run_publisher.bat` - 運行發佈者
- `run_receiver.bat` - 運行接收者

## 配置

默認配置使用公開的 Mosquitto 測試代理。可在代碼中修改以下參數：

```python
BROKER_ADDRESS = "test.mosquitto.org"  # MQTT 代理地址
BROKER_PORT = 1883                      # MQTT 代理端口
TOPIC = "test/topic"                    # 發佈/訂閱主題
AUTO_INTERVAL = 5                       # 自動發送間隔（秒）
```

## 工作原理

### 發佈者流程
1. 連接到 MQTT 代理
2. 啟動自動發送線程
3. 每 5 秒發送一條消息
4. 支持手動發送消息（可擴展功能）

### 接收者流程
1. 連接到 MQTT 代理
2. 訂閱指定的主題
3. 等待並顯示接收到的消息
4. 每秒更新一次狀態

## 代碼特點

- ✅ 線程安全的消息處理
- ✅ 跨平台支持（Windows、Linux、macOS）
- ✅ 完善的錯誤處理
- ✅ 清晰的日誌輸出

## 故障排除

**問題：無法連接到代理**
- 確保網絡連接正常
- 檢查代理地址和端口是否正確
- 嘗試使用不同的 MQTT 代理

**問題：收不到消息**
- 確保發佈者和接收者訂閱的主題相同
- 檢查發佈者是否成功連接
- 查看控制台的錯誤消息

## 擴展功能建議

- 添加用戶界面（GUI）
- 實現消息加密
- 添加數據庫存儲接收的消息
- 支持多個主題
- 實現自定義消息格式

## 許可證

此項目僅供學習使用。

## 參考資源

- [MQTT 官方文檔](https://mqtt.org/)
- [Eclipse Paho Python 客戶端](https://eclipse.org/paho/clients/python/)
- [Mosquitto 測試代理](https://test.mosquitto.org/)

---

**作者**: Python MQTT 教程  
**建立日期**: 2026 年 2 月
