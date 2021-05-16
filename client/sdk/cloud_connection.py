from sdk.local_connection import LocalConnection
from sdk.rai_config import RAIConfig

class CloudConnection(LocalConnection):
    def __init__(
        self,
        compute_name:str,
        dbname:str,
        open_mode:str="OPEN",
        verify_ssl:bool=True,
        scheme:str="https",
        config:RAIConfig=RAIConfig(),
        debug_level:int=0
    ):
        self.compute_name = compute_name
        self.config = config
        self.verify_ssl = verify_ssl
        super().__init__(dbname, open_mode, scheme, config.host, config.port, debug_level)
