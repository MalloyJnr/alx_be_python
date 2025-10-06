# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- REQUIRED: General Addition Test (for tool compatibility) ---
    def test_addition(self):
        """Basic tests for the add method to satisfy required test name."""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- Detailed Addition Tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-3, 5), 2)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    # --- Subtraction Tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -5), 2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(-3, 5), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)

    # --- Multiplication Tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(-3, 6), -18)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Division Tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))  # Returns None on division by zero

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
