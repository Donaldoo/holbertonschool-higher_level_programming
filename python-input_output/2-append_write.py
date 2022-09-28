#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """Appends text at the end of a file and count chars added"""
    with open(filename, "a", encoding="UTF8") as myFile:
        myFile.write(text)
        charCount = 0
        for char in text:
            charCount += 1
    return charCount
