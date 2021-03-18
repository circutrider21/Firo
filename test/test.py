import Firo
import unittest

class Testfiro(unittest.TestCase):
    con = Firo.Start("Test.db")
    def test_get(self):
        self.con.set("hy", "ha")
        self.assertEqual(self.con.get("hy"), "ha", "Values Should Match")
    def test_version(self):
        self.assertEqual(self.con.version(), "1.2", "Version should be the same as the test")
    
    def test_update(self):
        self.con.update("hy", "ho")
        self.assertEqual(self.con.get("hy"), "ho", "Values should be updates")

if __name__ == '__main__':
    unittest.main()
