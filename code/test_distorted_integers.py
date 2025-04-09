import unittest
import distorted_ints as di
import operator

class Normal(unittest.TestCase):
    # creation (with values)
    # tostring
    # multiply

    def setUp(self):
        self.i = di.DistortedInt(2, 5, 3)

    def test_creation(self):
        self.assertEqual(self.i.x, 2)
        self.assertEqual(self.i.a, 3)
        self.assertEqual(self.i.n, 5)
    
    def test_to_string(self):
        s = str(self.i)
        self.assertEqual(s, "<2 mod 5 | 3>")
    
    def test_multiply(self):
        j = di.DistortedInt(4, 5, 3)
        k = self.i * j # <3 mod 5 | 3>
        self.assertEqual(k.x, 3)
        self.assertEqual(k.a, 3)
        self.assertEqual(k.n, 5)

class Extreme(unittest.TestCase):
    # creation:
    #   - non integer
    #   - out of bounds
    # mul:
    #   - different a and n
    # eq:
    #   - values same and different

    def test_create_non_integer(self):
        # string
        self.assertRaises(TypeError, di.DistortedInt, "2", 3, 2)
        self.assertRaises(TypeError, di.DistortedInt, 2, "3", 2)
        self.assertRaises(TypeError, di.DistortedInt, 2, 3, "2")
        # float
        self.assertRaises(TypeError, di.DistortedInt, 2.0, 3, 2)
        self.assertRaises(TypeError, di.DistortedInt, 2, 3.0, 2)
        self.assertRaises(TypeError, di.DistortedInt, 2, 3, 2.0)
    
    def test_create_out_of_bounds(self):
        # n: n > 0
        self.assertRaises(ValueError, di.DistortedInt, 0, -1, 0)
        self.assertRaises(ValueError, di.DistortedInt, 0,  0, 0)
        di.DistortedInt(0, 1, 0)
        # a, x: 0 <= a,x < n
        i = di.DistortedInt(2, 3, -1)
        self.assertEqual(i.a, 2)
        i = di.DistortedInt(2, 3, 0)
        self.assertEqual(i.a, 0)
        i = di.DistortedInt(2, 3, 3)
        self.assertEqual(i.a, 0)

        i = di.DistortedInt(-1, 3, 2)
        self.assertEqual(i.x, 2)
        i = di.DistortedInt(0, 3, 2)
        self.assertEqual(i.x, 0)
        i = di.DistortedInt(3, 3, 2)
        self.assertEqual(i.x, 0)
    
    def test_mul_diff(self):
        i = di.DistortedInt(2, 5, 3)
        j = di.DistortedInt(1, 4, 3) # same a as i, diff n
        k = di.DistortedInt(2, 5, 2) # same n as i, diff a
        self.assertRaises(ValueError, operator.__mul__, i, j)
        self.assertRaises(ValueError, operator.__mul__, i, k)
    
    def test_eq(self):
        a = di.DistortedInt(2, 5, 3)
        b = di.DistortedInt(1, 5, 3)
        c = di.DistortedInt(2, 4, 3)
        d = di.DistortedInt(2, 5, 2)
        e = di.DistortedInt(2, 5, 3)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(a, d)
        self.assertEqual(a, e)

if __name__ == "__main__":
    unittest.main()