from openapi_client.api.default_api import DefaultApi
from openapi_client.models import *

class DelveClient(DefaultApi):

    def __init__(self, connection):
        self.conn = connection
        super().__init__()

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
                if name == act.name:
                    return act.result

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

        action_res = self.run_action(action=action, readonly=True)
        return action_res.rels

    def list_source(self):
        action = ListSourceAction(type=ListSourceAction.__name__)
        action_res = self.run_action(action=action, readonly=True)

        return action_res.get("sources")

    def query(self, queryString: str, isReadOnly: bool, outputs: list, inputs: list, actionName: str):
        source = Source(type=Source.__name__)
        source.type = 'Source'
        source.name = 'query'
        source.path = ''
        source.value = queryString

        action = QueryAction(type=QueryAction.__name__, source=source)
        action.inputs = inputs
        action.outputs = outputs
        action.persist = []

        action_res = self.run_action(action=action, readonly=True)
        return action_res.rels
