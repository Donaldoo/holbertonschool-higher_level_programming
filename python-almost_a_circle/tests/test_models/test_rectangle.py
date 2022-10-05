#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test class for rectangle class"""
    def test_rectangle_width_height(self):
        """create a rectangle with height and height"""
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)


    def test_rectangle_width_height_x(self):
        """create a rectangle with heigh, weight and x"""
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(4, 5, 6)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_width_height_x_y(self):
        """create a rectangle with height, width, x, y"""
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_width_str(self):
        """test width as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle("one", 2)

    def test_rectangle_height_str(self):
        """test height as  str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "two")
