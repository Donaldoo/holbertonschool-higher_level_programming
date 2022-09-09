#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    args_sum = 0
    while i != len(argv):
        args_sum += int(argv[i])
        i += 1
    print("{}".format(args_sum))
