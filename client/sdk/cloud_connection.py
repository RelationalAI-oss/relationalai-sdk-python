from sdk.local_connection import LocalConnection
from sdk.rai_credentials import RAICredentials

class CloudConnection(LocalConnection):
    def __init__(
        self,
        compute_name:str,
        dbname:str,
        open_mode:str="OPEN",
        verify_ssl:bool=True,
        scheme:str="http",
        creds:RAICredentials=RAICredentials(),
        debug_level:int=0
    ):
        self.compute_name = compute_name
        self.region = creds.region
        self.verify_ssl = verify_ssl
        self.infra = creds.infra

        super().__init__(dbname, open_mode, scheme, creds.host, creds.port, debug_level)

