#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    return sorted(a_dictionary.keys(), key=lambda scr: a_dictionary[scr])[-1]
