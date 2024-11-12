from ...base_client import BaseAPIClient

class DeviceAPI(BaseAPIClient):
    def get_iced_list(self):
        return self.post('/API/ICED/GetICEDList', json={})

    def control_door(self, device_ids: list, operate: int):
        return self.post('/API/Device/ICED/ControlDoor', json={
            "data": {
                "IDs": device_ids,
                "Operate": operate
            }
        })
