from relationalai.connection_base import ConnectionBase
from relationalai.rai_config import RAIConfig
from relationalai.management_client import RAIComputeFilters, RAIDatabaseFilters, RAIComputeSize

class ManagementConnection(ConnectionBase):
    def __init__(
        self,
        verify_ssl:bool=True,
        scheme:str="https",
        config:RAIConfig=None,
        debug_level:int=0
    ):
        self.config = config if config else RAIConfig().parse_config()
        super().__init__(scheme=scheme, host=self.config.host, port=self.config.port, debug_level=debug_level)
        self.verify_ssl = verify_ssl
        # work around circular dependency
        from relationalai import ManagementClient

        self.client = ManagementClient(self)
        self.client.api_client.configuration.host = self.base_url

    def list_computes(self, filters=RAIComputeFilters()):
        return self.client.list_computes(filters=filters)

    def list_databases(self, filters=RAIDatabaseFilters()):
        return self.client.list_databases(filters=filters)

    def list_users(self):
        return self.client.list_users()

    def list_compute_events(self, compute_id:str):
        return self.client.list_compute_events(compute_id=compute_id)

    def create_user(self, username:str):
        return self.client.create_user(username=username)

    def create_compute(self, compute_name:str, size:RAIComputeSize, region:str=None):
        return self.client.create_compute(compute_name=compute_name, size=size, region=region)

    def delete_compute(self, compute_name):
        return self.client.delete_compute(compute_name=compute_name)

    def remove_default_compute(self, dbname:str):
        return self.client.remove_default_compute(dbname=dbname)

    def get_account_credit_usage(self, period:str="current_month"):
        return self.client.get_account_credit_usage(period=period)