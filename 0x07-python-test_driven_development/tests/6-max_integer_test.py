#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """A class to test the max_integer function."""

    def test_empty_list(self):
        """Test that the function returns None for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_item_list(self):
        """Test that the function returns the single item in a list."""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_item_list(self):
        """Test that the function returns the max integer in a list."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)

    def test_non_integer_list(self):
        """Test that the function raises a TypeError for a non-integer list."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4, 5])

    def test_function_docstring(self):
        """Test that the function has a docstring."""
        self.assertIsNotNone(max_integer.__doc__)
    
    def test_function_docstring(self):
        """Test that the module has a docstring."""
        self.assertIsNotNone(__import__('6-max_integer').__doc__)

if __name__ == '__main__':
    unittest.main()