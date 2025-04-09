import unittest
import distorted_ints as di

class Arguments(unittest.TestCase):
    # n  n > 0

    def test_n(self):
        di.DistortedRootsOfOne(1, 0)
        di.DistortedRootsOfOne(50, 0)
        self.assertRaises(ValueError, di.DistortedRootsOfOne, 0, 0)
        self.assertRaises(ValueError, di.DistortedRootsOfOne, -1, 0)

class Normal(unittest.TestCase):
    # n to 100
    
    def test_n_to_hundred(self):
        for n in range(1, 101): # n {1, 2, ..., 100}
            for alpha in range(n): # a {0, 1, ..., n - 1}
                roots = di.DistortedRootsOfOne(n, alpha)
                self.assertEqual(len(roots), 1, "n %d a %d" % (n, alpha))
                i = roots[0]
                e = di.DistortedInt(1, n, alpha) # expected
                self.assertEqual(i, e)

if __name__ == "__main__":
    unittest.main()