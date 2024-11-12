from .system import SystemAPI
from .device import DeviceAPI
from .io import IOAPI

class ICADClient:
    def __init__(self, config):
        self.system = SystemAPI(config)
        self.device = DeviceAPI(config)
        self.io = IOAPI(config)
        
    def authenticate(self, user_id: str, password: str):
        """Authenticate and store credentials across all APIs"""
        auth_result = self.system.login(user_id, password)
        if auth_result["IsSuccess"]:
            self.device.user_id = self.system.user_id
            self.device.token = self.system.token
            self.io.user_id = self.system.user_id 
            self.io.token = self.system.token
        return auth_result
