from delve import LocalConnection

import unittest
import datetime

class TestQuery(unittest.TestCase):

    def toRelation(self, name, values, keys, columns):
        return {"rel_key": {"values": values, "name": name, "keys": keys, "type": "RelKey"}, "type": "Relation", "columns": columns}

    def testQuery(self):
        conn = LocalConnection(dbname="python-sdk")
        conn.debug_level = 1
        self.assertTrue(
            conn.query("def bar = 2", outputs=["bar"]).get("output")[0]
            == self.toRelation(name="bar", values=["Int64"], keys=[], columns=[[2]])
        )
        self.assertTrue(
            conn.query("def p = {(1,); (2,); (3,)}", outputs=["p"]).get("output")[0]
            == self.toRelation(name="p", values=[], keys=["Int64"], columns=[[1, 2, 3]])
        )
        self.assertTrue(
            conn.query("def p = {(1.1,); (2.2,); (3.4,)}", outputs=["p"]).get("output")[0]
            == self.toRelation(name="p", values=[], keys=["Float64"], columns=[[1.1, 2.2, 3.4]])
        )
        self.assertTrue(
            conn.query("def p = {(parse_decimal[64, 2, \"1.1\"],); (parse_decimal[64, 2, \"2.2\"],); (parse_decimal[64, 2, \"3.4\"],)}", outputs=["p"]).get("output")[0]
            == self.toRelation(name="p", values=[], keys=["FixedPointDecimals.FixedDecimal{Int64,2}"], columns=[[1.1, 2.2, 3.4]])
        )
        self.assertTrue(
            conn.query("def p = {(parse_decimal[64, 2, \"1.1\"],); (parse_decimal[64, 2, \"2.2\"],); (parse_decimal[64, 2, \"3.4\"],)}", outputs=["p"]).get("output")[0]
            == self.toRelation(name="p", values=[], keys=["FixedPointDecimals.FixedDecimal{Int64,2}"], columns=[[1.1, 2.2, 3.4]])
        )
        self.assertTrue(
            conn.query("def p = {(1, 5); (2, 7); (3, 9)}", outputs=["p"]).get("output")[0]
            == self.toRelation(name="p", values=[], keys=["Int64", "Int64"], columns=[[1, 2, 3], [5, 7, 9]])
        )

if __name__ == '__main__':
    unittest.main()