from sdk.connection import Connection

class LocalConnection(Connection):

    def __init__(
        self,
        dbname: str,
        open_mode: str = "OPEN",
        scheme: str = "http",
        host: str = "127.0.0.1",
        port: int = 8010,
        debug_level= 0
    ):
        super().__init__(scheme, host, port, debug_level)
        self.dbname = dbname
        self.open_mode = open_mode