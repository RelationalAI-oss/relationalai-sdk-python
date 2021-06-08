from delve import LocalConnection

import unittest
import datetime

class TestStatus(unittest.TestCase):

    def testStatus(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.status())

if __name__ == '__main__':
    unittest.main()