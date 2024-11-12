from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class PlatformConfig:
    base_url: str
    mqtt_broker: str
    mqtt_port: int
    mqtt_username: Optional[str] = None
    mqtt_password: Optional[str] = None

class Config:
    PLATFORMS = {
        'platform1': PlatformConfig(
            base_url='http://192.168.1.100:8080',
            mqtt_broker='mqtt.platform1.com',
            mqtt_port=1883
        ),
        'platform2': PlatformConfig(
            base_url='http://192.168.1.200:8080',
            mqtt_broker='mqtt.platform2.com',
            mqtt_port=1883
        )
    }
