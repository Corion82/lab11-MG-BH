# https://github.com/Corion82/lab11-MG-BH
# Partner 1: Matthew Gardstein
# Partner 2: Brent Hiser

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(1, -2), -1)
        self.assertEqual(calculator.add(1, 0), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(1, -10), 11)
        self.assertEqual(calculator.subtract(1, 4), -3)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 5), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(calculator.div(2, 10), 5.0)
        self.assertEqual(calculator.div(4, 20), 5.0)
        self.assertEqual(calculator.div(5, 0), 0.0)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 2)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(10, 100), 2)
        self.assertEqual(calculator.logarithm(2, 4096), 12)
        self.assertEqual(calculator.logarithm(5, 125), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(5, -10)
        # use same technique from test_divide_by_zero
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            calculator.square_root(-4)
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
