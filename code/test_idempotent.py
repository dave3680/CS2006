import unittest
import distorted_ints as di

class Normal(unittest.TestCase):

    def test_n(self):
        for n in range (1, 100):
            for alpha in range(0,n):
                self.assertTrue(di.HasDistortedIdempotentProperty(n, alpha))

if __name__ == "__main__":
    unittest.main()