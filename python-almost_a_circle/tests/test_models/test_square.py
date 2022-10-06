#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for square class"""
    def test_square_one(self):
        """test 1 arg"""
        sq1 = Square(1)
        sq2 = Square(2)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_two(self):
        """test 2 args"""
        sq1 = Square(1, 2)
        sq2 = Square(2, 3)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_three(self):
        """test 3 args"""
        sq1 = Square(1, 2, 3)
        sq2 = Square(3, 4, 5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_four(self):
        """test 4 args"""
        sq1 = Square(1, 2, 3, 10)
        sq2 = Square(3, 4, 5, 11)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_str_size(self):
        with self.assertRaises(TypeError):
            sq1 = Square("one")

    def test_square_str_arg(self):
        with self.assertRaises(TypeError):
            sq1 = Square(1, "two")

    def test_square_str_x(self):
        with self.assertRaises(TypeError):
            sq1 = Square(1, 2, "three")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(-1)

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            sq1 = Square(1, -2)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            sq1 = Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(0)
