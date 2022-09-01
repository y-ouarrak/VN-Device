from .utils import config
from .core import client

client.connect(config.get('mqtt_host'), config.get('mqtt_port'))
