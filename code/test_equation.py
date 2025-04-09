import unittest
import distorted_ints as di

class Normal(unittest.TestCase):
    # n < 0
    # (3, 0) (3, 1)

    def test_n(self):
        self.assertRaises(ValueError, di.HasDistortedEquationProperty, -1, 0)
        self.assertRaises(ValueError, di.HasDistortedEquationProperty, 0, 0)
        di.HasDistortedEquationProperty(1, 0)
    
    def test_normal(self):
        self.assertTrue(di.HasDistortedEquationProperty(3, 0))
        self.assertFalse(di.HasDistortedEquationProperty(3, 1))

if __name__ == "__main__":
    unittest.main()