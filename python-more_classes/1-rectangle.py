#!/usr/bin/python3
"""Task 1"""


class Rectangle:
    """New class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @width.setter
        def width(self, value):
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @height.setter
        def height(self, value):
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
