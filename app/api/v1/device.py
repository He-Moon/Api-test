from .base_client import BaseAPIClient

class DeviceAPI(BaseAPIClient):
    def get_device_list(self):
        return self.get('/api/devices')
    
    def get_device_info(self, device_id: str):
        return self.get(f'/api/devices/{device_id}')
