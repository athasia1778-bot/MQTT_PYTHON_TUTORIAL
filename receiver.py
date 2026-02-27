import os
import json
import paho.mqtt.client as mqtt
import time


def load_config():
    cfg = {
        "BROKER_ADDRESS": "test.mosquitto.org",
        "BROKER_PORT": 1883,
        "TOPIC": "test/topic",
    }
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except Exception:
        pass

    try:
        if os.path.exists("config.json"):
            with open("config.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict):
                cfg.update({k: v for k, v in data.items() if v is not None})
    except Exception as e:
        print(f"[RECEIVER] Failed to read config.json: {e}")

    cfg["BROKER_ADDRESS"] = os.getenv("MQTT_BROKER", cfg["BROKER_ADDRESS"])
    try:
        cfg["BROKER_PORT"] = int(os.getenv("MQTT_PORT", cfg["BROKER_PORT"]))
    except Exception:
        cfg["BROKER_PORT"] = cfg["BROKER_PORT"]
    cfg["TOPIC"] = os.getenv("MQTT_TOPIC", cfg["TOPIC"])

    return cfg


_CFG = load_config()
BROKER_ADDRESS = _CFG["BROKER_ADDRESS"]
BROKER_PORT = _CFG["BROKER_PORT"]
TOPIC = _CFG["TOPIC"]

new_message = False


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[RECEIVER] Connected to {BROKER_ADDRESS}:{BROKER_PORT}")
        client.subscribe(TOPIC)
        print(f"[RECEIVER] Subscribed to {TOPIC}")
    else:
        print(f"[RECEIVER] Connection failed, rc={rc}")


def on_message(client, userdata, msg):
    global new_message
    new_message = True
    print(f"[RECEIVER] Received message: {msg.payload.decode()}")


def main():
    global new_message
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_start()

    try:
        while True:
            if not new_message:
                print("[RECEIVER] N/A")
            new_message = False
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
