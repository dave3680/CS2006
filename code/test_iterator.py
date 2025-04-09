import unittest
import distorted_ints as di

class Normal(unittest.TestCase):

    def test_idempotent(self):
         for n in range (1, 100):
            for alpha in range(0,n):
                self.assertTrue(di.HasDistortedIdempotentPropertyIterator(n, alpha))

    
    def test_commutative(self):
        self.assertTrue(di.IsCommutativeDistortedMultiplicationIterator(7,4))
        self.assertFalse(di.IsCommutativeDistortedMultiplicationIterator(21,10))

    def test_associative(self):
        self.assertTrue(di.IsAssociativeDistortedMultiplicationIterator(3, 0))
        self.assertTrue(di.IsAssociativeDistortedMultiplicationIterator(3, 1))
        self.assertFalse(di.IsAssociativeDistortedMultiplicationIterator(56, 67))

    def test_quasi(self):
        self.assertTrue(di.IsQuasiDistributiveDistortedMultiplication(6, 4))
        self.assertFalse(di.IsQuasiDistributiveDistortedMultiplication(56, 67))


if __name__ == "__main__":
    unittest.main()