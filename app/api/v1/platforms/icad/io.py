from typing import Dict, List
from ...base_client import BaseAPIClient

class IOAPI(BaseAPIClient):
    def get_io_list(self, iced_ids: List[int]) -> Dict:
        """Get IO device list for specified ICED devices"""
        return self.post("/API/IO/GetIOList", {
            "ICEDID": iced_ids
        }).json()

    def update_io_relationships(self, device_id: int, relationships: List[Dict]) -> Dict:
        """Update IO relationships for a device"""
        return self.post("/API/IO/UpdateIORelationships", {
            "ID": device_id,
            "Relationship": relationships
        }).json()
