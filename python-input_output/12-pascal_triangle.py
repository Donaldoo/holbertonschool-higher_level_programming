#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    """pascal's triangle"""
    new_list = []
    if n <= 0:
        return new_list

    for i in range(n):
        row = [1]
        if new_list:
            last_row = new_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        new_list.append(row)
    return new_list
