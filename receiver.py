import paho.mqtt.client as mqtt
import time

BROKER_ADDRESS = "test.mosquitto.org"
BROKER_PORT = 1883
TOPIC = "test/topic"

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
