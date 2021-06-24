from relationalai import LocalConnection

import unittest

class TestSetOptions(unittest.TestCase):

    def testSetOptions(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.configure(debug=True))

if __name__ == '__main__':
    unittest.main()
