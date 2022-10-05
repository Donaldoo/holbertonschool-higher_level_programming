#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test class for rectangle class"""
    def test_rectangle_width_height(self):
        """test rectangle with height and height"""
        rect1 = Rectangle(1, 2)
        self.assertEqual(1, rect1.id)

    def test_rectangle_width_height_x(self):
        """test rectangle with heigh, weight and x"""
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_width_height_x_y(self):
        """test rectangle with height, width, x, y"""
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_all_args(self):
        """test if rect with all 5 args exists"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, rect1.id)

    def test_rectangle_width_str(self):
        """test width as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle("one", 2)

    def test_rectangle_height_str(self):
        """test height as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "two")

    def test_rect_x_str(self):
        """test rect with x as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, "three")

    def test_rect_y_str(self):
        """test rect with y as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, 3, "four")

    def test_negative_width(self):
        """test rect with negative width"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 2)

    def test_negative_height(self):
        """test rect with negative height"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, -2)

    def test_neg_x(self):
        """test rect with negative x"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, -3)

    def test_neg_y(self):
        """test rect with negative y"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, 3, -4)

    def test_width_zero(self):
        """test rect with width 0"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 1)

    def test_height_zero(self):
        """test rect with height 0"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 0)

    def test_area(self):
        """test rect area"""
        r1 = Rectangle(1, 2)
        self.assertEqual(2, r1.area())
