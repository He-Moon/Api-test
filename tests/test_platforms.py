from config import PlatformAConfig, PlatformBConfig
from app.api.v1.platforms.platform_a import PlatformAClient
from app.api.v1.platforms.platform_b import PlatformBClient

def test_platform_a():
    client = PlatformAClient(PlatformAConfig)
    response = client.get_specific_data()
    assert response.status_code == 200

def test_platform_b():
    client = PlatformBClient(PlatformBConfig)
    response = client.get_other_data()
    assert response.status_code == 200
