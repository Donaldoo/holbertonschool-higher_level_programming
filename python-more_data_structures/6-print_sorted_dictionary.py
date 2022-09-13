#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict is None:
        return
    for key, i in sorted(my_dict.items()):
        print("{}: {}".format(key, i))
