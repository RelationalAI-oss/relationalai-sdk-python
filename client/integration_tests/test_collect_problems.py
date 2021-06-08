from delve import LocalConnection

import unittest
import datetime

class TestCollectProblems(unittest.TestCase):

    def testCollectProblems(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(len(conn.collect_problems()) == 0)
        conn.install_source("name", "def foo =")
        self.assertTrue(len(conn.collect_problems()) == 2)

if __name__ == '__main__':
    unittest.main()