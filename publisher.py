import paho.mqtt.client as mqtt
import threading
import time
import sys

BROKER_ADDRESS = "test.mosquitto.org"
BROKER_PORT = 1883
TOPIC = "test/topic"

# interval for automatic messages (seconds)
AUTO_INTERVAL = 5

client = None
stop_event = threading.Event()
# lock used to coordinate printing/input so messages don't interrupt typing
print_lock = threading.Lock()


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[PUBLISHER] Connected to {BROKER_ADDRESS}:{BROKER_PORT}")
    else:
        print(f"[PUBLISHER] Connection failed, rc={rc}")


def on_publish(client, userdata, mid, properties=None):
    # MQTT v5 callback signature does not include rc; mid is the only required
    # argument beyond client/userdata.  Older versions passed rc, which caused
    # `missing 1 required positional argument: 'rc'` errors with newer paho
    # releases.  We log whatever information is available.
    print(f"[PUBLISHER] Message published (mid={mid})")


def auto_publish_thread():
    print("[PUBLISHER] Auto-publish thread started")
    count = 0
    while not stop_event.is_set():
        try:
            count += 1
            msg = f"Auto Message #{count}"
            client.publish(TOPIC, msg)
            with print_lock:
                print(f"[PUBLISHER] Auto published: {msg}")
            time.sleep(AUTO_INTERVAL)
        except Exception as e:
            with print_lock:
                print(f"[PUBLISHER] Error: {e}")
    print("[PUBLISHER] Auto-publish thread stopped")


def main():
    global client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_start()

    # start auto thread
    thread = threading.Thread(target=auto_publish_thread, daemon=True)
    thread.start()

    with print_lock:
        print("[PUBLISHER] Enter messages to publish (Ctrl+C to exit):")
    try:
        while True:
            # hold the lock while prompting/reading so the auto thread
            # won't write mid‑sentence
            with print_lock:
                message = input()
            if message:
                client.publish(TOPIC, message)
                with print_lock:
                    print(f"[PUBLISHER] Published user message: {message}")
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        client.loop_stop()
        client.disconnect()
        print("[PUBLISHER] Exiting")


if __name__ == "__main__":
    main()