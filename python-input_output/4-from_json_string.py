#!/usr/bin/python3
"""Task 4"""
import json


def from_json_string(my_str):
    """return an object represented by a json string"""
    return json.loads(my_str)
