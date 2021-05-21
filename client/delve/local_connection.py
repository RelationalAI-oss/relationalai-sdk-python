from delve.connection import Connection

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

        # work around circular dependency
        from delve.delve_client import DelveClient
        self.client = DelveClient(self)
        self.client.api_client.configuration.host = self.base_url


    def cardinality(self, rel_name: str = None):
        return self.client.cardinality(rel_name)
    
    def clone_database(self, source_name: str, overwrite: bool = False):
        return self.client.clone_database(source_name, overwrite)

    def create_database(self, overwrite: bool = False):
        return self.client.create_database(overwrite)

    def delete_source(self, source_name: str):
        return self.client.delete_source(source_name)
    
    def install_source(self, src_name:str="", src_str:str="", src_path:str=""):
        return self.client.install_source(src_name=src_name, src_str=src_str, src_path=src_path)
    
    def list_edb(self, rel_name: str = None):
        return self.client.list_edb(rel_name)

    def list_source(self):
        return self.client.list_source()

    def query(self, src: str = "", action_name: str = "query", readonly: bool = True, inputs: list = [], outputs: list = [], persist: list = []):
        return self.client.query(src, action_name, readonly, inputs, outputs, persist)