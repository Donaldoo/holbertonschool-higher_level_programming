#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test class for rectangle class"""
    def test_rectangle_width_height(self):
        """create a rectangle with height and height"""
        self.rect1 = Rectangle(1, 2)

    def test_rectangle_width_height_x(self):
        """create a rectangle with heigh, weight and x"""
        self.rect1 = Rectangle(1, 2, 3)

    def test_rectangle_width_height_x_y(self):
        """create a rectangle with height, width, x, y"""
        self.rect1 = Rectangle(1, 2, 3, 4)

    def test_rectangle_width_str(self):
        """test width as str"""
        self.rect1 = Rectangle("one", 2)

    def test_rectangle_height_str(self):
        """test height as  str"""
        self.rect1 = Rectangle(1, "two")
