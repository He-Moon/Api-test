from app.api.v1.platform_client import PlatformClient

def test_platform1():
    client = PlatformClient('platform1')
    response = client.get_device_list()
    assert response.status_code == 200

def test_platform2():
    client = PlatformClient('platform2')
    response = client.get_system_status()
    assert response.status_code == 200
