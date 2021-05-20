import sys
sys.path.append("../client")

from openapi_client.api.default_api import DefaultApi
from openapi_client.api_client import ApiClient
from openapi_client.model.create_compute_request_protocol import CreateComputeRequestProtocol
from openapi_client.model.delete_compute_request_protocol import DeleteComputeRequestProtocol
from sdk import RAIRequest, RAIConfig

class RAIComputeFilters(object):
    def __init__(self, id:list=[], name:list=[], size:list=[], state:list=[]):
        self.id = id
        self.name = name
        self.size = size
        self.state = state

class RAIDatabaseFilters(object):
    def __init__(self, id:list=[], name:list=[], state:list=[]):
        self.id = id
        self.name = name
        self.state = state

class RAIComputeSize(object):
    def __init__(self, compute_size="XS"):
        self.rai_compute_sizes = {
            "XS":"XS",
            "S":"S",
            "M":"M",
            "L":"L",
            "XL":"XL"
        }
        self.size = compute_size

    @property
    def size(self):
        return self.__size

    @size.getter
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            self.__size = self.rai_compute_sizes[value]
        except:
            raise Exception("{} unknown compute type.".format(value))

class ApiClientOverload(ApiClient):
    def __init__(
        self,
        sign=False,
        extra_headers=dict(),
        rai_config=None,
        debug_level=0
    ):
        super().__init__()
        self.sign = sign
        self.extra_headers = extra_headers
        self.config = rai_config
        self.debug_level = debug_level

    def request(self, method, url, query_params=[], headers=dict(),
                post_params=None, body={}, _preload_content=True,
                _request_timeout=None):

        headers.update(self.extra_headers)

        rai_request = RAIRequest(
            rai_config=self.config,
            method=method,
            url=url,
            query_params=query_params,
            headers=headers,
            post_params=post_params,
            body=body,
            _preload_content=True,
            _request_timeout=None
        )

        if self.sign:
            rai_request.sign(debug_level=self.debug_level)

        if self.debug_level > 0:
            print("=> Request:")
            print("=> Method: {}".format(rai_request.method))
            print("=> url: {}".format(rai_request.url))
            print("=> headers: {}".format(rai_request.headers))
            print("=> body: {}".format(rai_request.body))
            print("=> query_params: {}".format(rai_request.query_params))

        return super().request(
            method=rai_request.method,
            url=rai_request.url,
            query_params=rai_request.query_params,
            headers=rai_request.headers,
            post_params=rai_request.post_params,
            body=rai_request.body,
            _preload_content=rai_request._preload_content,
            _request_timeout=rai_request._request_timeout
        )

class DelveCloudClient(DefaultApi):
    def __init__(self, connection):
        self.conn = connection
        extra_headers = {"Content-Type": "application/json", "Host": self.conn.config.host}
        api_client = ApiClientOverload(sign=True, extra_headers=extra_headers, rai_config=self.conn.config, debug_level=self.conn.debug_level)
        super().__init__(api_client=api_client)

    def list_computes(self, filters=RAIComputeFilters()):
        return self.compute_get(id=filters.id, name=filters.name, size=filters.size, state=filters.state)

    def list_databases(self, filters=RAIDatabaseFilters()):
        return self.database_get(id=filters.id, name=filters.name, state=filters.state)

    def create_compute(self, compute_name:str, size:RAIComputeSize, region:str=None, dry_run=False):
        region = region if region else self.conn.config.region
        create_compute_request_protocol = CreateComputeRequestProtocol(
            region=region,
            name=compute_name,
            size=size.size,
            dryrun=dry_run,
        )
        return self.compute_put(create_compute_request_protocol)

    def delete_compute(self, compute_name, dry_run=False):
        delete_compute_request_protocol = DeleteComputeRequestProtocol(
            name=compute_name,
            dryrun=True,
        )
        return self.compute_delete(delete_compute_request_protocol)
