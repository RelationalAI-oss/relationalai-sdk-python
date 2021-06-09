from relationalai import LocalConnection

import unittest

class TestCloneDatabase(unittest.TestCase):

    def toRelation(self, name, values, keys, columns):
        return {"rel_key": {"values": values, "name": name, "keys": keys, "type": "RelKey"}, "type": "Relation", "columns": columns}

    def testCloneDatabase(self):
        conn1 = LocalConnection(dbname="python-sdk-1")
        conn2 = LocalConnection(dbname="python-sdk-2")
        conn3 = LocalConnection(dbname="python-sdk-3")

        conn1.debug_level = 1
        conn2.debug_level = 1
        conn3.debug_level = 1

        self.assertTrue(conn1.create_database(overwrite=True))
        self.assertTrue(len(conn1.install_source(src_name="name", src_str="def x = {(1,); (2,); (3,)}").get("problems")) == 0)
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3]])
        )

        # clone from conn1 to conn2
        self.assertTrue(conn2.clone_database(source_name=conn1.dbname, overwrite=True))
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3]])
        )
        self.assertTrue(len(conn1.install_source(src_name="name", src_str="def x = {(1,); (2,); (3,); (4,)}").get("problems")) == 0)
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 4]])
        )
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3]])
        )

        self.assertTrue(len(conn2.install_source(src_name="name", src_str="def x = {(1,); (2,); (3,); (5,)}").get("problems")) == 0)
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 4]])
        )
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 5]])
        )

        # DBConnection overload, cloning from conn1 to conn3
        self.assertTrue(conn3.clone_database(source_name=conn1.dbname, overwrite=True))
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 4]])
        )
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 5]])
        )
        self.assertTrue(
            conn3.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 4]])
        )

        # clone from conn2 to conn3, overwriting conn3 in the process
        self.assertTrue(conn3.clone_database(source_name=conn2.dbname, overwrite=True))
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 4]])
        )
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 5]])
        )
        self.assertTrue(
            conn3.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=[], keys=["Int64"], columns=[[1, 2, 3, 5]])
        )

        # clone database
        conn1.create_database(overwrite=True)
        conn2.create_database(overwrite=True)

        self.assertTrue(len(conn1.install_source(src_name="name", src_str="def x = {(1,)}").get("problems")) == 0)
        self.assertTrue(len(conn2.install_source(src_name="name", src_str="def x = {(2,)}").get("problems")) == 0)

        self.assertTrue(conn2.clone_database(source_name=conn1.dbname, overwrite=True))
        self.assertTrue(
            conn1.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=["Int64"], keys=[], columns=[[1]])
        )
        self.assertTrue(
            conn2.query(outputs=["x"]).get("output")[0]
            == self.toRelation(name="x", values=["Int64"], keys=[], columns=[[1]])
        )

if __name__ == '__main__':
    unittest.main()
