#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        my_list = [1, 2, 3, 4, 5]
        result = max_integer(my_list)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        my_list = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, my_list)

    def test_empty(self):
        """Test with an empty list: should return None"""
        my_list = []
        result = max_integer(my_list)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        my_list = [-2, -6, -1]
        result = max_integer(my_list)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        my_list = [3, 4.5, 2]
        result = max_integer(my_list)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        my_list = [45]
        result = max_integer(my_list)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        my_list = [8, 8, 8, 8, 8]
        result = max_integer(my_list)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        my_list = ["hi", "hello"]
        result = max_integer(my_list)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
