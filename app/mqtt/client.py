import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
    
    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
