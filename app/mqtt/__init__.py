import paho.mqtt.client as mqtt
from typing import Callable
from ..config import PlatformConfig

class MQTTHandler:
    def __init__(self, platform_config: PlatformConfig):
        self.client = mqtt.Client()
        self.broker = platform_config.mqtt_broker
        self.port = platform_config.mqtt_port
        
        if platform_config.mqtt_username:
            self.client.username_pw_set(
                platform_config.mqtt_username,
                platform_config.mqtt_password
            )
    
    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
    
    def subscribe(self, topic: str, callback: Callable):
        def on_message(client, userdata, message):
            callback(message.payload.decode())
        
        self.client.subscribe(topic)
        self.client.on_message = on_message
