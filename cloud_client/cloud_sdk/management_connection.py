import sys
sys.path.append("../client")

from sdk.connection import Connection
from sdk.rai_config import RAIConfig
from cloud_sdk.delve_cloud_client import RAIComputeFilters, RAIDatabaseFilters, RAIComputeSize

class ManagementConnection(Connection):
    def __init__(
        self,
        verify_ssl:bool=True,
        scheme:str="https",
        config:RAIConfig=RAIConfig(),
        debug_level:int=0
    ):
        super().__init__(scheme=scheme, host=config.host, port=config.port, debug_level=debug_level)

        self.verify_ssl = verify_ssl
        self.config = config
        # work around circular dependency
        from cloud_sdk import DelveCloudClient

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