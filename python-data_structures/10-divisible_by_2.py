#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        div = []
        if i % 2 == 0:
            div.append(True)
        else:
            div.append(False)
    return div
