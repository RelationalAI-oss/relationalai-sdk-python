from relationalai import LocalConnection

import unittest

class TestEnableLibrary(unittest.TestCase):

    def testEnableLibrary(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(conn.enable_library("stdlib"))

if __name__ == '__main__':
    unittest.main()
