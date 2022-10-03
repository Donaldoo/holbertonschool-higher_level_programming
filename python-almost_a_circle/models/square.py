#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)
