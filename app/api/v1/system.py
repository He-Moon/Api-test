from .base_client import BaseAPIClient

class SystemAPI(BaseAPIClient):
    def get_system_status(self):
        return self.get('/api/system/status')
    
    def get_system_info(self):
        return self.get('/api/system/info')
