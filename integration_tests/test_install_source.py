from relationalai import LocalConnection

import os
import tempfile
import unittest

class TestInstallSource(unittest.TestCase):

    def testInstallSource(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(len(conn.install_source(src_name="src_1", src_str="def foo = 1").get("problems")) == 0)

        # create a tempfile
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, "w") as tmp:
            tmp.write("def bar = 3")
        self.assertTrue(len(conn.install_source(src_name="src_3", src_path=path).get("problems")) == 0)
        self.assertTrue(len(conn.install_source(src_name="src_2", src_str="def foo = ").get("problems")) == 2)

if __name__ == '__main__':
    unittest.main()
