from delve import LocalConnection

import unittest
import datetime

class TestCardinality(unittest.TestCase):

    def toRelation(self, name, values, keys, columns):
        return {"rel_key": {"values": values, "name": name, "keys": keys, "type": "RelKey"}, "type": "Relation", "columns": columns}

    def testCardinality(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(conn.create_database(overwrite=True))
        self.assertTrue(len(conn.query("def p = {(1,); (2,); (3,)}", persist=["p"], readonly=False).get("problems")) == 0)
        self.assertTrue(
            conn.cardinality("p").get("result")[0]
            == self.toRelation(name="p", values=[], keys=["Int64"], columns=[[3]])
        )
        self.assertTrue(conn.delete_edb("p"))
        self.assertTrue(conn.cardinality("p").get("result") == [])

if __name__ == '__main__':
    unittest.main()