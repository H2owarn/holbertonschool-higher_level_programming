#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_positive2_numbers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))  # Should return None

    def test_duplicate_max_values(self):
        self.assertEqual(max_integer([5, 5, 3, 5, 2]), 5)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([3, 1, 4, 1, 5, 9, 2]), 9)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 1234567]), 1234567)

if __name__ == "__main__":
    unittest.main()