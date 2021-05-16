from openapi_client.api.default_api import DefaultApi
from openapi_client.api_client import ApiClient
from openapi_client.models import *

from sdk.rai_request import RAIRequest
from sdk.rai_credentials import RAICredentials

class ApiClientOverload(ApiClient):

    def __init__(self, extra_headers:dict=dict(), extra_params:dict=dict()):
        super().__init__()
        self.extra_headers = extra_headers
        self.extra_params = extra_params

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):

        RAIRequest.sign(headers, query_params, method, url, "{}", debug_level=3)
        return super().request(method, url, query_params, headers, post_params, body, _preload_content, _request_timeout)


class DelveClient(DefaultApi):

    def __init__(self, connection):
        self.conn = connection
        api_client = ApiClientOverload()
        super().__init__(api_client=api_client)

    def run_action(self, action: Action, readonly: bool, name: str = "single", open_mode: str = "OPEN"):
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
                    return act.get("result")

        return None

    def cardinality(self, relname: str):
        action = CardinalityAction(type=CardinalityAction.__name__)
        action.relname = relname

        action_res = self.run_action(action=action, readonly=True)
        return action_res

    def clone_database(self, source_name: str, overwrite: bool):
        xact = Transaction()
        xact.mode = "CLONE_OVERWRITE" if overwrite else "CLONE"
        xact.dbname = self.conn.dbname
        xact.actions = []
        xact.source_dbname = source_dbname
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

    def delete_source(self, source_name: str, actionName: str = 'action'):
        action = ModifyWorkspaceAction(type=ModifyWorkspaceAction.__name__)
        action.delete_source = [source_name]

        action_res = self.run_action(action=action, readonly=False)
        return action_res

    def install_source(self, source_name: str, source_str: str, actionName:str):
        source = Source(type=Source.__name__)
        source.name = source_name
        source.value = source_str
        
        action = InstallAction(type=InstallAction.__name__)
        action.sources = [source]

        action_res = self.run_action(action=action, readonly=False)
        return action_res

    def list_edb(self, relname: str = None):
        action = ListEdbAction(type=ListEdbAction.__name__)
        action.relname = relname if relname else None

        action_res = self.run_action(action=action, readonly = True)
        return action_res.get("rels")

    def list_source(self):
        action = ListSourceAction(type=ListSourceAction.__name__)
        action_res = self.run_action(action=action, readonly=True)

        return action_res.get("sources")

    def query(self, src: str, action_name, readonly: bool = True, inputs: list = [], outputs: list = [], persist: list = []):
        source = Source(type=Source.__name__)
        source.name = action_name
        source.path = ""
        source.value = src

        action = QueryAction(type=QueryAction.__name__, source=source)
        action.inputs = inputs
        action.outputs = outputs
        action.persist = persist

        action_res = self.run_action(action=action, readonly=True)
        return action_res["output"]
