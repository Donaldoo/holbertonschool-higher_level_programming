#!/usr/bin/python3
"""Task 10"""


class Student:
    """New class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}
            for el in attrs:
                if el in self.__dict__:
                    new_dict[el] = self.__dict__[el]
            return new_dict
        return self.__dict__
