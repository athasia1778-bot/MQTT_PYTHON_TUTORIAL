# MQTT Python 教程

這是一個簡單的 MQTT（消息佇列遙測傳輸）Python 實現教程項目，演示了發佈者-訂閱者模式的基本用法。

## 項目描述

本項目包含一個完整的 MQTT 應用示例，包括：
# MQTT Python 教程

此儲存庫包含一個以 Python 撰寫的簡明 MQTT 教學範例，示範如何使用 `paho-mqtt` 實作發佈/訂閱模式，並提供可在本機或 Docker 中運行的範例。

## 專案內容

- main.py — 可同時啟動 publisher 與 receiver 的啟動程式
- publisher.py — 範例發佈者，週期性傳送訊息
- receiver.py — 範例訂閱者，列印接收到的訊息
- run_publisher.bat / run_receiver.bat — Windows 快捷執行檔
- requirements.txt — 範例所需套件

## 先決條件

- Python 3.8 或以上
- Git（非必需）
- Docker 與 docker-compose（選用，用於本機 Mosquitto broker）

## 快速上手（建議）

1. 建立並啟動虛擬環境：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. 安裝相依套件：

```powershell
pip install -r requirements.txt
```

3. 在一個終端啟動接收者，另一個終端啟動發佈者：

```powershell
python receiver.py
python publisher.py
```

發佈者會將訊息送到 MQTT broker，接收者會即時列印接收到的訊息。

## 設定（修改 broker/port/topic）

可透過下列方式修改設定：

- 編輯 config.json（建議）、或
- 設定環境變數： MQTT_BROKER / MQTT_PORT / MQTT_TOPIC / MQTT_AUTO_INTERVAL

範例（config.json 或程式頂部預設）：

```json
{
	"BROKER_ADDRESS": "test.mosquitto.org",
	"BROKER_PORT": 1883,
	"TOPIC": "test/topic",
	"AUTO_INTERVAL": 5
}
```

或以環境變數覆蓋：

```powershell
$env:MQTT_BROKER = "localhost"
$env:MQTT_PORT = "1883"
$env:MQTT_TOPIC = "my/topic"
```

## 使用 Docker 在本機啟動 Mosquitto（選用）

建立一個 docker-compose.yml（下方為簡單範例），用以同時啟動 Mosquitto broker：

```yaml
version: '3'
services:
	mosquitto:
		image: eclipse-mosquitto:2.0
		ports:
			- "1883:1883"
		volumes:
			- ./mosquitto.conf:/mosquitto/config/mosquitto.conf:ro
```

啟動 broker：

```powershell
docker-compose up -d
```

將設定中的 BROKER_ADDRESS 改為 localhost，然後執行 Python 腳本。

## 測試

建議使用 pytest 建置簡單的整合測試流程：啟動測試 broker、由 publisher 發送測試訊息，並由 receiver 驗證是否接收。執行測試：

```powershell
pytest -q
```

## 疑難排解

- 若發佈者無法連線：請確認 BROKER_ADDRESS、BROKER_PORT 以及網路連線狀態。
- 若無法接收訊息：請確認發佈者與接收者使用相同 TOPIC、QoS 設定正確。
- 需要詳細日誌：可在程式中啟用 logging 或直接於終端觀察輸出。

## 後續建議

- 新增 .env 或 config.example.json 並將程式改為讀取配置檔（已提供範例）。
- 提供 docker-compose.yml 與 mosquitto.conf 以重現本機環境。
- 建立 pytest 測試以及 GitHub Actions 工作流程以執行 CI。
- 增加簡短的 Jupyter Notebook，說明本範例中使用的 MQTT 概念。

## 貢獻

歡迎提出改進或 PR，請先建立 issue 討論主要變更。

---

檔案： [README.md](README.md)

建立： 2026-02
## Next steps / suggested improvements

- Add a `.env` / `config.example.json` for configuration
- Provide a `docker-compose.yml` and `mosquitto.conf` for a reproducible local environment
- Add `pytest` integration tests and GitHub Actions workflow
- Add a short Jupyter Notebook explaining MQTT concepts used in the demo

## Contributing

Contributions and improvements are welcome — please open an issue or PR.

---

File: [README.md](README.md)

Created: 2026-02
---
