import paho.mqtt.client as mqtt
from ..utils import config


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


client = mqtt.Client(config.get('mqtt_client'))  # client ID "mqtt-test"
client.on_message = on_message
client.on_connect = on_connect
client.on_connect_fail = on_connect

client.username_pw_set(config.get('mqtt_user'), config.get('mqtt_passwd'))
