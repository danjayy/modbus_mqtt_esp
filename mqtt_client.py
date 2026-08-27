import paho.mqtt.client as mqtt

BROKER_HOST = "*********"
BROKER_PORT = 1883


def on_connect(ma, client, userdata, flags, rc):
    print(f"1 {ma}")
    if rc == 0:
        print("Connected to MQTT broker")
        print(f"2 {ma}")

        client.subscribe("devices/sensor/state")
        # client.publish("device/command", "ON")
    else:
        print(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    print(f"Received [{msg.topic}]: {msg.payload.decode()}")
    print(type(msg.payload.decode()))


try:
    mclient = mqtt.Client()

    mclient.on_connect = lambda client, username, flags, rc: on_connect("heyyy worldd", client, username, flags, rc)
    mclient.on_message = on_message

    mclient.connect(BROKER_HOST, BROKER_PORT)

    mclient.loop_forever()
except KeyboardInterrupt:
    mclient.disconnect()

