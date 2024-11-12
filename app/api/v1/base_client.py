import logging
import requests
from typing import Optional, Dict, Any

class BaseAPIClient:
    def __init__(self, config):
        self.base_url = config.base_url
        self.user_id: Optional[str] = None
        self.token: Optional[str] = None
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def _get_auth_params(self) -> Dict[str, str]:
        return {
            "UserID": self.user_id,
            "Token": self.token
        } if self.user_id and self.token else {}
        
    def post(self, endpoint: str, data: Dict[str, Any] = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        json_data = {"UserID": self.user_id, "Token": self.token}
        if data:
            json_data["data"] = data
            
        self.logger.debug(f"Request to {endpoint}: {json_data}")
        try:
            response = requests.post(url, json=json_data)
            response.raise_for_status()
            result = response.json()
            self.logger.debug(f"Response from {endpoint}: {result}")
            return result
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise
    
    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, data=data, headers=self.headers)
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, headers=self.headers)