from openapi_client.api.default_api import DefaultApi
from openapi_client.models.action import Action
from openapi_client.models.transaction import Transaction
from openapi_client.models.labeled_action import LabeledAction

class DelveClient(DefaultApi):

    def __init__(self, connection):
        self.conn = connection
        super().__init__()

    def run_action(self, conn, name: str, action: Action, is_readonly: bool, open_mode: str):
        xact = Transaction()
        xact.mode = open_mode
        xact.dbname = conn.dbname
        xact.readonly = is_readonly
        xact.version = conn.version

        labeled_action = LabeledAction()
        labeled_action.name = name
        labeled_action.action = action
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
        response_version = resopnse.version
        if (response_version > current_version):
            self.conn.version = response_version

        if (not response.aborted):
            for act in response.actions:
                if name == act.name:
                    return act.result

        return None


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
