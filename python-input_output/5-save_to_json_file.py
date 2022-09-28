#!/usr/bin/python3
"""Task 5"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text files, using json representation"""
    with open(filename, "w", encoding="UTF8") as myFile:
        json_obj = json.dumps(my_obj)
        myFile.write(json_obj)
