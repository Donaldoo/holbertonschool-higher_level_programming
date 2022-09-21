"""Unittest"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittet for max integer"""
    def max_at_end(self):
        numbers = [1, 2, 4, 3, 5]
        self.assertEqual(max_integer(max_at_end), 5)

    def max_at_beginning(self):
        numbers = [5, 2, 3, 4]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def max_in_middle(self):
        numbers = [1, 2, 5, 4, 3]
        self.assertEqual(max_integer(max_at_middle), 5)

    def negative_in_list(self):
        number = [1, 2, -3, 5]
        self.assertEqual(max_integer(negative_in_list), 5)

    def only_negative(self):
        number = [-1, -2, -3, -4]
        self.assertEqual(max_integer(only_negative), -1)

    def one_el(self):
        number = [4]
        self.assertEqual(max_integer(one_el), 4)
