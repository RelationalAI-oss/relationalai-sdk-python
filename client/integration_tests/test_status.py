from delve import LocalConnection

import unittest
import datetime

class TestStatus(unittest.TestCase):

    def testStatus(self):
        conn = LocalConnection(dbname="python-sdk")
        self.assertTrue(conn.status())

if __name__ == '__main__':
    unittest.main()