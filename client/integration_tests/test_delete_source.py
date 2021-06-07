from delve import LocalConnection

import unittest
import datetime

class TestDeleteSource(unittest.TestCase):

    def testDeleteSource(self):
        conn = LocalConnection(dbname="python-sdk")
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(conn.delete_source(source_name="stdlib"))

if __name__ == '__main__':
    unittest.main()