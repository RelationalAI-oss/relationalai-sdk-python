from delve.connection import Connection
from delve.rai_config import RAIConfig
from delve.delve_cloud_client import RAIComputeFilters, RAIDatabaseFilters, RAIComputeSize

class ManagementConnection(Connection):
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
        from delve import DelveCloudClient

        self.client = DelveCloudClient(self)
        self.client.api_client.configuration.host = self.base_url

    def list_computes(self, filters=RAIComputeFilters()):
        return self.client.list_computes(filters=filters)

    def list_databases(self, filters=RAIDatabaseFilters()):
        return self.client.list_databases(filters=filters)

    def create_compute(self, compute_name:str, size:RAIComputeSize, region:str=None):
        return self.client.create_compute(compute_name=compute_name, size=size, region=region)

    def delete_compute(self, compute_name):
        return self.client.delete_compute(compute_name=compute_name)