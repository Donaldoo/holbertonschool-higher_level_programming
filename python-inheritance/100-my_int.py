#!/usr/bin/python3
"""Task 12"""


class MyInt(int):
    """New class MyInt"""
    def __new__(cls, value):
        """Create new object"""
        return super().__new__(cls, value)

    def __eq__(self, value):
        if super().__eq__(value):
            return False
        return True
 
    def __ne__(self, value):
        if self.__eq__(value):
            return False
        return True
