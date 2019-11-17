import test_runge_kutta
import unittest

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromModule(test_runge_kutta)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
