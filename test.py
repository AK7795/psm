import sqlite3
import unittest

class c1(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("pms.db")
        self.code ="11"
        self.name = "ak"
    def tearDown(self):
        self.code="0"
        self.name = ""
        self.con.close()

    def test1(self):
        res = self.con.execute("SELECT name FROM patient WHERE code = "+self.code)
        for i in res:
            fetchname =i[0]

        self.assertEqual(fetchname,self.name)

if __name__ == "__main__":
    unittest.main()