#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """Writes text to a file and counts chars written"""
    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(text)
        charCount = 0
        for char in text:
            charCount += 1
    return charCount
