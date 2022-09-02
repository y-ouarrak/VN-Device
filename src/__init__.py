from time import sleep
from .utils import config
from .core import client

client.connect(config.get('mqtt_host'), config.get('mqtt_port'))

with open('events.csv') as events:
    for row in events:
        print(config.get('mqtt_topic'))
        print(client.publish(config.get('mqtt_topic'),
                             row.replace('\n', '').encode().hex().upper()))
        sleep(config.get('wait_time'))
