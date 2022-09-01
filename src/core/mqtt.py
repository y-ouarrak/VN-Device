import paho.mqtt.client as mqtt
from ..utils import config

client = mqtt.Client(config.get('mqtt_client_id')) # client ID "mqtt-test"
client.username_pw_set(config.get('mqtt_user'), config.get('mqtt_passwd'))

