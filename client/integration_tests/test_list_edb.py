from delve import LocalConnection

import unittest
import datetime

class TestListEdb(unittest.TestCase):

    def testListEdb(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(len(conn.list_edb().get("rels")) == 0)

if __name__ == '__main__':
    unittest.main()