#!/usr/bin/python3
"""Task 1"""


class Base:
    """New class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
