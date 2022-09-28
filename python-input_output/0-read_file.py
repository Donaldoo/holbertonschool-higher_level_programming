#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """Opens and read a file"""
    with open(filename, encoding="utf-8") as myFile:
        readData = myFile.read()
        print(readData, end="")
