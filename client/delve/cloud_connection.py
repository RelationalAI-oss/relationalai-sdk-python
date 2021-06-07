from delve.management_connection import ManagementConnection
from delve.local_connection import LocalConnection
from delve.rai_config import RAIConfig

class CloudConnection(LocalConnection):
    def __init__(
        self,
        compute_name:str,
        dbname:str,
        open_mode:str="OPEN",
        scheme:str="https",
        mngt_conn:ManagementConnection=None,
        debug_level:int=0
    ):
        self.compute_name = compute_name
        self.config = mngt_conn.config
        self.verify_ssl = mngt_conn.verify_ssl

        super().__init__(dbname, open_mode, scheme, self.config.host, self.config.port, debug_level)
