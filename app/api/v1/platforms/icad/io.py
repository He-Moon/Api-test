from ...base_client import BaseAPIClient

class IOAPI(BaseAPIClient):
    def get_io_list(self, iced_ids: list):
        return self.post('/API/IO/GetIOList', json={
            "data": {
                "ICEDID": iced_ids
            }
        })
