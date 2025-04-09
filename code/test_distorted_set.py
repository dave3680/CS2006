import unittest
import distorted_int_set as dis
import distorted_ints as di

class Arguments(unittest.TestCase):
    # n > 0
    # 0 <= a < n

    def test_n(self):
        dis.DistortedIntSet(1, 0)
        self.assertRaises(ValueError, dis.DistortedIntSet, 0, 0)
        self.assertRaises(ValueError, dis.DistortedIntSet, -1, 0)
    
    def test_a(self):
        dis.DistortedIntSet(5, 0)
        dis.DistortedIntSet(5, 2)
        dis.DistortedIntSet(5, 4)
        dis.DistortedIntSet(5, -1)
        dis.DistortedIntSet(5, 5)
        dis.DistortedIntSet(5, 6)

class Normal(unittest.TestCase):
    # to_list
    # size
    # str

    def test_to_list(self):
        self.assertEqual([di.DistortedInt(0, 1, 0)], dis.DistortedIntSet(1, 0).to_list())
        self.assertEqual([di.DistortedInt(0, 3, 1), di.DistortedInt(1, 3, 1), di.DistortedInt(2, 3, 1)], 
                         dis.DistortedIntSet(3, 1).to_list())
        self.assertEqual(20, len(dis.DistortedIntSet(20, 0).to_list()))
        self.assertEqual(2000, len(dis.DistortedIntSet(2000, 5).to_list()))
    
    def test_size(self):
        self.assertEqual(1, dis.DistortedIntSet(1, 0).size())
        self.assertEqual(20, dis.DistortedIntSet(20, 0).size())
        self.assertEqual(2000, dis.DistortedIntSet(2000, 5).size())

    def test_str(self):
        self.assertEqual("<[0] mod 1 | 0>", str(dis.DistortedIntSet(1, 0)))
        self.assertEqual("<[0, 1, 2] mod 3 | 1>", str(dis.DistortedIntSet(3, 1)))

    def test_repr(self):
        self.assertEqual("[<0 mod 1 | 0>]", repr(dis.DistortedIntSet(1, 0)))
        self.assertEqual("[<0 mod 3 | 1>, <1 mod 3 | 1>, <2 mod 3 | 1>]", repr(dis.DistortedIntSet(3, 1)))


if __name__ == "__main__":
    unittest.main()