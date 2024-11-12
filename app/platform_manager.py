from .config import Config, PlatformConfig
from .api.system_api import SystemAPI
from .api.device_api import DeviceAPI
from .mqtt.mqtt_client import MQTTHandler

class PlatformManager:
    def __init__(self, platform_name: str):
        if platform_name not in Config.PLATFORMS:
            raise ValueError(f"Platform {platform_name} not found in configuration")
        
        self.config: PlatformConfig = Config.PLATFORMS[platform_name]
        self.system_api = SystemAPI(self.config)
        self.device_api = DeviceAPI(self.config)
        self.mqtt_handler = MQTTHandler(self.config)
