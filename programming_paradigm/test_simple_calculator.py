# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Required Test Names ---
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):  # ✅ Renamed for checker compatibility
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertIsNone(self.calc.divide(10, 0))

    # --- Additional Addition Tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-3, 5), 2)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Additional Subtraction Tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -5), 2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(-3, 5), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)

    # --- Additional Multiplication Tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 6), -18)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Additional Division Tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))  # Returns None

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
