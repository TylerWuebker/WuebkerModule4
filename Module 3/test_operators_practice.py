import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        a = 7
        b = -2
        self.assertFalse(a == b)
    def test_notequal_operator(self):
        a = 8
        b = 8
        self.assertTrue(a != b)
    def test_greater_than(self):
        a = 7
        b = 6
        self.assertTrue(a > b)
    def test_less_than(self):
        a = 7
        b = 6
        self.assertFalse(a < b)
    def test_greather_than_equal(self):
        a = 2
        b = 2
        self.assertTrue(a <= b)
    def test_less_than_equal(self):
        a = 2
        b = 3
        self.assertFalse(a <= b)

if __name__ == '__main__':
    unittest.main()
