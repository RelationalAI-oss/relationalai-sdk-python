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
        self.debug_level = debug_level
        self.version = None

    def set_connection_on_client():
        if self.client:
            self.client.conn = self