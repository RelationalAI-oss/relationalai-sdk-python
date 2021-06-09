from relationalai import LocalConnection
from openapi_client.exceptions import ApiException

import unittest

class TestCreateDatabase(unittest.TestCase):

    def testCreateDatabase(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))

        with self.assertRaises(ApiException):
            conn.create_database()

if __name__ == '__main__':
    unittest.main()