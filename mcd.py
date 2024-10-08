import unittest

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def MCD4N(a, b, c, d):
    return mcd(mcd(mcd(a, b), c), d)

class TestMCD(unittest.TestCase):
    
    def test_MCD2N(self):
        self.assertEqual(mcd(54, 24), 6)
        self.assertEqual(mcd(48, 18), 6)
        self.assertEqual(mcd(101, 103), 1)
        self.assertEqual(mcd(25, 5), 5)
    
    def test_MCD4N(self):
        self.assertEqual(MCD4N(120, 80, 40, 20), 20)
        self.assertEqual(MCD4N(100, 10, 50, 25), 5)
        self.assertEqual(MCD4N(17, 19, 23, 29), 1)
        self.assertEqual(MCD4N(60, 48, 36, 24), 12)

    def test_MCD0N(self):
        self.assertEqual(mcd(3, 0), 3)
        self.assertEqual(mcd(0, 9), 9)

if __name__ == '__main__':
    unittest.main()
