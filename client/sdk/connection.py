from sdk.delve_client import DelveClient

class Connection(object):

    def __init__(
        self,
        scheme: str = "http",
        host: str = "127.0.0.1",
        port: int = 8010,
        debug_level: int = 0
    ):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.base_url = "{}://{}:{}".format(scheme, host, port)
        self.debug_level = debug_level
        self.client = DelveClient(self)
        self.client.api_client.configuration.host = self.base_url
        self.version = 0
