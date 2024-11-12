    from .system import SystemAPI
    from .device import DeviceAPI
    from .io import IOAPI

    class ICADClient:
        def __init__(self, config):
            self.system = SystemAPI(config)
            self.device = DeviceAPI(config)
            self.io = IOAPI(config)
