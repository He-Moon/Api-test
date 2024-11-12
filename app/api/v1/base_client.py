import requests

class BaseAPIClient:
    def __init__(self):
        self.base_url = None
        self.headers = {}
        self.session = requests.Session()
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params, headers=self.headers)
    
    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, headers=self.headers)
    
    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, data=data, headers=self.headers)
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, headers=self.headers)
