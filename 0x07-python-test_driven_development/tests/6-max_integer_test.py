#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class that tests the max_integer module
    Using Unittests
    """
    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer("ahmed"), 'm')
    
    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, -1, -100, -3, -5]), 0)

    def test_rep(self):
        self.assertEqual(max_integer([0, 0, 1, 1, 4, 6, 6]), 6)
        self.assertEqual(max_integer([-100, -3, 100, 9, 4, 0, -100, 100, 100]), 100)

    def test_empty(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
    
    def test_exception(self):
        self.assertRaises(TypeError, max_integer, ["aaa", 1, "ahmed"])
        self.assertRaises(TypeError, max_integer, 5)

if __name__ == "__main__":
    unittest.main()
