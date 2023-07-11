#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(max_integer([1, 2, 3])), int)

    def test_value(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
