from ...base_client import BaseAPIClient

class SystemAPI(BaseAPIClient):
    def login(self, user_id: str, password: str):
        return self.post('/API/System/Login', json={
            "data": {
                "UserID": user_id,
                "Password": password
            }
        })

    def project_sign_in(self, project_id: int):
        return self.post('/API/System/ProjectSignIn', json={
            "data": {
                "ProjectID": project_id
            }
        })

    def get_project_list(self):
        return self.post('/API/System/GetProject2', json={
            "data": {}
        })
