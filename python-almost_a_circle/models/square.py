#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """assigns attributes to args"""
        attr = ["id", "size", "x", "y"]
        if args:
            for a in range(len(args)):
                setattr(self, attr[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dect represantion of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
