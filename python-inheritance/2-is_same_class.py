#!/usr/bin/python3
"""Task 2"""


def is_same_class(obj, a_class):
    """Checks if object is an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
