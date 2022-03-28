import sqlite3
import unittest

class c1(unittest.TestCase):

    def setUp(self):
        self.con = sqlite3.connect("employee.db")
        self.code ="11"
        self.name = "akash"
    def tearDown(self):
        self.code="0"
        self.name = ""
        self.con.close()

    def test1(self):
        res = self.con.execute("SELECT empname FROM empdata WHERE empcode = "+self.code)
        for i in res:
            fetchname =i[0]

        self.assertEqual(fetchname,self.name)

if __name__ == "__main__":
    unittest.main()