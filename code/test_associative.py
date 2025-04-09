import unittest
import distorted_ints as di

class Normal(unittest.TestCase):
    # n  n > 0
    # n=3, a=1,2
    # get pairs

    def test_n(self):
        di.IsAssociativeDistortedMultiplication(1, 0)
        di.IsAssociativeDistortedMultiplication(20, 0)
        self.assertRaises(ValueError, di.IsAssociativeDistortedMultiplication, 0, 0)
        self.assertRaises(ValueError, di.IsAssociativeDistortedMultiplication, -1, 0)
    
    def test_n_three(self):
        # know for n=3, if a=0,1 assoc. true, a=2 assoc false
        self.assertTrue(di.IsAssociativeDistortedMultiplication(3, 0))
        self.assertTrue(di.IsAssociativeDistortedMultiplication(3, 1))
        self.assertFalse(di.IsAssociativeDistortedMultiplication(3, 2))
    
    def test_get_pairs(self):
        pairs = di.getAssociativePairs()
        self.assertGreater(len(pairs),0)
        # check values for small scale, we know true for a = 0,1 and not true n=3, a=2
        pairs = di.getAssociativePairs(3)
        self.assertEqual([(1, 0), (2, 0), (2, 1), (3, 0), (3, 1)], pairs)

if __name__ == "__main__":
    unittest.main()