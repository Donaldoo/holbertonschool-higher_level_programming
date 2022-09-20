#!/usr/bin/python3
"""Task 2"""


def say_my_name(first_name, last_name=""):
    """prints My name is followed by first name and alst name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if first_name is None:
        first_name = ""
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name is None:
        last_name = ""

    print("My name is {} {}".format(first_name, last_name))
