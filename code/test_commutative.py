import unittest
import distorted_ints as di

class Normal(unittest.TestCase):

    def test_n(self):
        self.assertTrue(di.IsCommutativeDistortedMultiplication(7,4))
        self.assertFalse(di.IsCommutativeDistortedMultiplication(26,8))

if __name__ == "__main__":
    unittest.main()