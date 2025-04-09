import unittest
import test_distorted_integers, test_roots_of_one, test_associative # is this correct syntax?
import test_distorted_set, test_equation
import test_idempotent
import test_commutative
import test_quasi
import test_iterator

# howto add more test files
#   put filename in import
#   put filename in modules array

if __name__ == "__main__":
    # loader
    loader = unittest.TestLoader()
    # test suite
    suite = unittest.TestSuite()
    modules = [
        test_distorted_integers,
        test_roots_of_one,
        test_associative,
        test_distorted_set,
        test_idempotent,
        test_commutative,
        test_quasi,
        test_iterator,
        test_equation,

    ]
    for module in modules:
        suite.addTest(loader.loadTestsFromModule(module))
    # run
    unittest.TextTestRunner(verbosity=2).run(suite)