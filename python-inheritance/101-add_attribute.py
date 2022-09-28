#!/usr/bin/python3
"""task 13"""


def add_attribute(obj, name, value):
    """Adds new attr to obj"""
    if ("__dict__" in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
