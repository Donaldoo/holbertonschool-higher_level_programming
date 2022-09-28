#!/usr/bin/python3
"""Task 7"""
from os.path import exists
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_exists = exists("add_item.json")
if file_exists is True:
    new_file = load_from_json_file("add_item.json")
    new_list = new_file + argv[1:]
    save_to_json_file(new_list, "add_item.json")
else:
    save_to_json_file(argv[1:], "add_item.json")
