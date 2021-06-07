from delve import LocalConnection

import unittest
import datetime

class TestListSource(unittest.TestCase):

    def testListSource(self):
        conn = LocalConnection(dbname="python-sdk")
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(conn.list_source())

if __name__ == '__main__':
    unittest.main()