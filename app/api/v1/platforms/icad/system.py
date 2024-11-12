from typing import Dict
from ...base_client import BaseAPIClient

class SystemAPI(BaseAPIClient):
    def login(self, user_id: str, password: str) -> Dict:
        response = self.post("/API/System/Login", {
            "UserID": user_id,
            "Password": password
        })
        if response.status_code == 200:
            data = response.json()
            if data["IsSuccess"]:
                self.user_id = user_id
                self.token = data["data"]["Token"]
        return response.json()

    def project_sign_in(self, project_id: int) -> Dict:
        return self.post("/API/System/ProjectSignIn", {
            "ProjectID": project_id
        }).json()

    def get_projects(self) -> Dict:
        return self.post("/API/System/GetProject2").json()

    def ping(self) -> Dict:
        return self.post("/API/System/Ping").json()

    def logout(self) -> Dict:
        return self.post("/API/System/Logout").json()
