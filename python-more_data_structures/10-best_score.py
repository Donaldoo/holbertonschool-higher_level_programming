#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return sorted(a_dictionary, key=lambda score: score[2])[-1]
