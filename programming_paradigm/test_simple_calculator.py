#!/usr/bin/python3
"""
This module contains unit tests for the SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    Each method tests a corresponding method in the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up a SimpleCalculator instance before each test.
        This method is called before each test function is executed.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various scenarios."""
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(-5, -5), -10, "Should be -10")
        self.assertEqual(self.calc.add(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0, "Should be 4.0")

    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(-1, -1), 0, "Should be 0")
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "Should be 3.0")

    def test_multiplication(self):
        """Test the multiply method with various scenarios."""
        self.assertEqual(self.calc.multiply(3, 7), 21, "Should be 21")
        self.assertEqual(self.calc.multiply(-1, 1), -1, "Should be -1")
        self.assertEqual(self.calc.multiply(-5, -5), 25, "Should be 25")
        self.assertEqual(self.calc.multiply(10, 0), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0, "Should be 3.0")

    def test_division(self):
        """Test the divide method, including the division by zero edge case."""
        self.assertEqual(self.calc.divide(10, 2), 5, "Should be 5")
        self.assertEqual(self.calc.divide(-10, 2), -5, "Should be -5")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")
        self.assertEqual(self.calc.divide(0, 5), 0, "Should be 0")
        
        # Test for division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
        self.assertIsNone(self.calc.divide(0, 0), "Division by zero should return None")

if __name__ == '__main__':
    unittest.main()