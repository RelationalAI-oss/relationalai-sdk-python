from openapi_client.api.default_api import DefaultApi
from openapi_client.models.action import Action
from openapi_client.models.transaction import Transaction
from openapi_client.models.labeled_action import LabeledAction

from sdk.connection import Connection

class DelveClient(DefaultApi):

    def __init__(self, connection):
        self.conn = connection

    def run_action(self, conn: Connection, name: str, action: Action, is_readonly: bool, open_mode: str):
        xact = Transaction()
        xact.mode = open_mode
        xact.dbname = conn.dbname
        xact.readonly = is_readonly
        xact.version = conn.version

        labeled_action = LabeledAction()
        labeled_action.name = name
        labeled_action.action = action
        xact.actions = [labeled_action]

        response = transaction_post(xact)

    def create_database(self, overwrite: bool = False):
        xact = Transaction()
        xact.mode = "CREATE_OVERWRITE" if overwrite else "CREATE"
        xact.dbname = self.conn.dbname
        xact.actions = []

        response = transaction_post(xact)
