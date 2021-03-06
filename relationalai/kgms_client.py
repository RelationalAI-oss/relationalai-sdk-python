from rai_api.api.default_api import DefaultApi
from rai_api.api_client import ApiClient
from rai_api.models import *

from relationalai.rai_request import RAIRequest
from relationalai.rai_credentials import RAICredentials
from relationalai.connection import Connection

import os

class ApiClientOverload(ApiClient):
    def __init__(self, sign=False, rai_config=None, extra_headers:dict=dict(), extra_params:list=[], debug_level=0):
        super().__init__()
        self.sign = sign
        self.config = rai_config
        self.extra_headers = extra_headers
        self.extra_params = extra_params
        self.debug_level = debug_level

    def request(self, method, url, query_params=[], headers=dict(),
                post_params=None, body={}, _preload_content=True,
                _request_timeout=None):

        headers.update(self.extra_headers)
        query_params = query_params + self.extra_params
        if "mode" in body.keys():
            query_params = query_params + [("open_mode", body.get("mode"))]
        if "source_dbname" in body.keys():
            query_params = query_params + [("source_dbname", body.get("source_dbname"))]

        rai_request = RAIRequest(
            rai_config=self.config,
            method=method,
            url=url,
            query_params=query_params,
            headers=headers,
            post_params=post_params,
            body=body,
            _preload_content=True,
            _request_timeout=None,
            service="transaction"
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

class KGMSClient(DefaultApi):
    def __init__(self, connection):
        self.conn = connection
        api_client = None

        if isinstance(self.conn, Connection):
            extra_headers = {"Host": self.conn.config.host}
            extra_params = [("compute_name", self.conn.compute_name), ("dbname", self.conn.dbname), ("region", self.conn.config.region)]
            api_client = ApiClientOverload(
                sign=True,
                rai_config=self.conn.config,
                extra_headers=extra_headers,
                extra_params=extra_params,
                debug_level=self.conn.debug_level
            )
        else:
            api_client = ApiClientOverload(debug_level=self.conn.debug_level)

        super().__init__(api_client=api_client)

    def __read_file_from_path(self, src):
        if src.path:
            if not src.name:
                src.name = os.path.basename(src.path)
            if (not src.value) and (os.path.isfile(src.path)):
                with open(src.path) as f:
                    src.value = f.read()

    def run_action(self, action, readonly: bool, name: str = "single", open_mode: str = "OPEN"):
        xact = Transaction()
        xact.mode = open_mode
        xact.dbname = self.conn.dbname
        xact.readonly = readonly
        xact.debug_level = self.conn.debug_level
        xact.version = self.conn.version
        
        labeled_action = LabeledAction(action=action, name=name)
        xact.actions = [labeled_action]

        if (self.conn.debug_level > 0):
            print("=> Transaction: {}".format(xact))

        response = self.transaction_post(xact)

        if (self.conn.debug_level > 0):
            print("=> TransactionResult: {}".format(response))

        # Sync the reported database version to our local
        # connection version. Important, as we want to ensure
        # that in subsequent transactions this will be the
        # minimum required version of the database. Note that
        # only write transactions bump the version.
        current_version = self.conn.version if self.conn.version else 0
        response_version = response.version
        if (response_version > current_version):
            self.conn.version = response_version

        if (not response.aborted):
            for act in response.actions:
                if name == act.get("name"):
                        return {"result": act.get("result"), "problems": response.problems}

        return None

    def status(self):
        action = StatusAction(type=StatusAction.__name__)
        return self.run_action(action, readonly=True) != None

    def cardinality(self, relname: str):
        action = CardinalityAction(type=CardinalityAction.__name__)
        action.relname = relname

        action_res = self.run_action(action=action, readonly=True)
        return {"result": action_res.get("result").get("result"), "problems": action_res.get("problems")}

    def clone_database(self, source_name: str, overwrite: bool):
        xact = Transaction()
        xact.mode = "CLONE_OVERWRITE" if overwrite else "CLONE"
        xact.dbname = self.conn.dbname
        xact.actions = []
        xact.source_dbname = source_name
        xact.readonly = False

        response = self.transaction_post(xact)

        if (response.problems):
            raise Exception(response.problems)

        return not response.aborted

    def create_database(self, overwrite: bool = False):
        xact = Transaction()
        xact.mode = "CREATE_OVERWRITE" if overwrite else "CREATE"
        xact.dbname = self.conn.dbname
        xact.actions = []

        if (self.conn.debug_level > 0):
            print("=> Transaction: {}".format(xact))

        response = self.transaction_post(xact)

        if (self.conn.debug_level > 0):
            print("=> TransactionResult: {}".format(response))

        if (response.problems):
            raise Exception(response.problems)

        return not response.aborted

    def delete_source(self, source_name: str):
        action = ModifyWorkspaceAction(type=ModifyWorkspaceAction.__name__)
        action.delete_source = [source_name]

        action_res = self.run_action(action=action, readonly=False)
        return action_res

    def install_source(self, src_name:str="", src_str:str="", src_path:str=""):
        source = Source(type=Source.__name__)
        source.name = src_name
        source.value = src_str
        source.path = src_path

        self.__read_file_from_path(source)

        action = InstallAction(type=InstallAction.__name__)
        action.sources = [source]

        action_res = self.run_action(action=action, readonly=False)
        return action_res

    def list_edb(self, relname: str = None):
        action = ListEdbAction(type=ListEdbAction.__name__)
        action.relname = relname if relname else None

        action_res = self.run_action(action=action, readonly = True)
        return {"rels": action_res.get("result").get("rels"), "problems": action_res.get("problems")}

    def list_source(self):
        action = ListSourceAction(type=ListSourceAction.__name__)
        action_res = self.run_action(action=action, readonly=True)

        return {"sources": action_res.get("result").get("sources"), "problems": action_res.get("problems")}

    def query(self, src: str="", action_name = "query", readonly: bool = True, inputs: list = [], outputs: list = [], persist: list = []):
        source = Source(type=Source.__name__)
        source.name = action_name
        source.path = ""
        source.value = src

        action = QueryAction(type=QueryAction.__name__, source=source)
        action.inputs = inputs
        action.outputs = outputs
        action.persist = persist

        action_res = self.run_action(action=action, readonly=readonly)
        return {"output": action_res.get("result").get("output"), "problems": action_res.get("problems")}

    def enable_library(self, src_name:str):
        action = ModifyWorkspaceAction(type=ModifyWorkspaceAction.__name__)
        action.enable_library = src_name

        action_res = self.run_action(action=action, readonly=True)
        return True if action_res else False

    def delete_edb(self, rel_name:str):
        action = ModifyWorkspaceAction(type=ModifyWorkspaceAction.__name__)
        action.delete_edb = rel_name

        action_res = self.run_action(action, readonly=False)
        return True if action_res else False

    def collect_problems(self):
        action = CollectProblemsAction(type=CollectProblemsAction.__name__)
        action_res = self.run_action(action=action, readonly=True)
        return action_res.get("result").get("problems")

    def configure(self, debug:bool=None, debug_trace:bool=None, silent:bool=None, abort_on_error:bool=None):
        action = SetOptionsAction(type=SetOptionsAction.__name__)
        action.debug = debug
        action.debug_trace = debug_trace
        action.silent = silent
        action.abort_on_error = abort_on_error

        action_res = self.run_action(action=action, readonly=False)
        return True if action_res else False
