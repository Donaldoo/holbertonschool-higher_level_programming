#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """prints sorted list"""
    def print_sorted(self):
        print(sorted(self))
