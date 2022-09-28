#!/usr/bin/python3
"""Task 12"""


class MyInt(int):
    """New class MyInt"""
    def __eq__(self, value):
        return self.other != value
    
    def __ne__(self, value):
        return self.other == value
