from relationalai.connection_base import ConnectionBase

class LocalConnection(ConnectionBase):
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
        from relationalai.kgms_client import KGMSClient
        self.client = KGMSClient(self)
        self.client.api_client.configuration.host = self.base_url


    def cardinality(self, rel_name: str = None):
        return self.client.cardinality(rel_name)

    def status(self):
        return self.client.status()
    
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

    def enable_library(self, src_name:str):
        return self.client.enable_library(src_name)

    def delete_edb(self, rel_name:str):
        return self.client.delete_edb(rel_name)

    def collect_problems(self):
        return self.client.collect_problems()

    def configure(self, debug:bool=None, debug_trace:bool=None, silent:bool=None, abort_on_error:bool=None):
        return self.client.configure(debug=debug, debug_trace=debug_trace, silent=silent, abort_on_error=abort_on_error)
