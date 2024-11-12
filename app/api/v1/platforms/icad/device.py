from typing import Dict, List
from ...base_client import BaseAPIClient

class DeviceAPI(BaseAPIClient):
    def get_iced_list(self) -> Dict:
        """Get list of ICED devices"""
        return self.post("/API/ICED/GetICEDList").json()

    def control_door(self, device_ids: List[int], operate: int) -> Dict:
        """Control door operation
        operate: 
            1 - normal open
            2 - normal close 
            3 - open once
            4 - force close
            5 - restore from force close
        """
        return self.post("/API/Device/ICED/ControlDoor", {
            "IDs": device_ids,
            "Operate": operate
        }).json()

    def control_relay(self, device_id: int, action: int, time: int = 0) -> Dict:
        """Control relay
        action:
            1 - Close Forever
            2 - Open Forever
            7 - Open for Duration
            8 - Close for Duration
        """
        return self.post("/API/ICED/ControlRelay", {
            "ID": device_id,
            "Action": action,
            "Time": time
        }).json()
