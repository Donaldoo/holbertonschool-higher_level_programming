#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, encoding="UTF8") as myFile:
        myObj = json.load(myFile)
