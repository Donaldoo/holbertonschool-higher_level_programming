"""Unittest"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittet for max integer"""
    def test_max_at_end(self):
        numbers = [1, 2, 4, 3, 5]
        self.assertEqual(max_integer(number), 5)

    def test_max_at_beginning(self):
        numbers = [5, 2, 3, 4]
        self.assertEqual(max_integer(number), 5)

    def test_max_in_middle(self):
        numbers = [1, 2, 5, 4, 3]
        self.assertEqual(max_integer(number), 5)

    def test_negative_in_list(self):
        number = [1, 2, -3, 5]
        self.assertEqual(max_integer(number), 5)

    def test_only_negative(self):
        number = [-1, -2, -3, -4]
        self.assertEqual(max_integer(number), -1)

    def test_one_el(self):
        number = [4]
        self.assertEqual(max_integer(number), 4)

    def test_empty_list(self):
        number = []
        self.assertEqual(max_integer(number), None)
