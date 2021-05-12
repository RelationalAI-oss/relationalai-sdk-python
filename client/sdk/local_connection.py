from sdk.connection import Connection

class LocalConnection(Connection):

    def __init__(
        self,
        dbname: str,
        open_mode: str = "OPEN",
        scheme: str = "http",
        host: str = "127.0.0.1",
        port: int = 8010,
        debug_level = 0
    ):
        super().__init__(scheme, host, port, debug_level)
        self.dbname = dbname
        self.open_mode = open_mode

    def create_database(self, overwrite: bool = False):
        return self.client.create_database(overwrite)

    def clone_database(self, source_name: str, overwrite: bool = False):
        return self.client.clone_database(source_name, overwrite)

    def cardinality(self, rel_name: str = None):
        return self.client.cardinality(rel_name)
    
    def list_edb(self, rel_name: str = None):
        return self.client.list_edb(rel_name)

    def list_source(self):
        return self.client.list_source()

    def query(self, queryString: str, isReadOnly: bool = True, outputs: list = ['out'], inputs: list = [], actionName = 'action'):
        return self.client.query(queryString, isReadOnly, outputs, inputs, actionName)
