import unittest
import distorted_ints as di

class Normal(unittest.TestCase):

    def test_n(self):
                self.assertTrue(di.IsQuasiDistributiveDistortedMultiplication(6, 4))
if __name__ == "__main__":
    unittest.main()