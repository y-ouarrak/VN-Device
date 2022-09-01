from dotenv import load_dotenv
from os import environ

load_dotenv()

config = {
    "mqtt_user": environ.get("MQTT_USER", ""),
    "mqtt_passwd": environ.get("MQTT_PASSWD", ""),
    "mqtt_host": environ.get("MQTT_HOST", "localhost"),
    "mqtt_port": int(environ.get("MQTT_PORT", 1883)),
    "mqtt_client": environ.get("MQTT_CLIENT_ID", "VM-Device"),
    "mqtt_topic": environ.get("MQTT_TOPIC", ""),
    "wait_time": int(str(environ.get("WAIT_TIME", 60))),
}
