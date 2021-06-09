from relationalai import LocalConnection

import unittest

class TestListSource(unittest.TestCase):

    def testListSource(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(conn.list_source())

if __name__ == '__main__':
    unittest.main()