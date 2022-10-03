#!/usr/bin/python3
"""Task 2"""
from models.base import Base


class Rectangle(Base):
    """New class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if self.__width is not int:
            raise TypeError("{} must be an integer".format(self.__width))
        if self.__width <= 0:
            raise ValueError("{} must be > 0".format(self.__width))
        self.__width = width

    @height.setter
    def height(self, height):
        if self.__height is not int:
            raise TypeError("{} must be an integer".format(self.__height))
        if self.__height <= 0:
            raise ValueError("{} must be > 0".format(self.__height))
        self.__height = height

    @x.setter
    def x(self, x):
        if self.__x is not int:
            raise TypeError("{} must be an integer".format(self.__x))
        if self.__x <= 0:
            raise ValueError("{} must be > 0".format(self.__x))
        self.__x = x

    @y.setter
    def y(self, y):
        if self.__y is not int:
            raise TypeError("{} must be an integer".format(self.__y))
        if self.__y <= 0:
            raise ValueError("{} must be > 0".format(self.__y))
        self.__y = y
