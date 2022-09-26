#!/usr/bin/python3
def magic_string(s=[0]):
    s[0] += 1
    return (", ".join(["Holberton" for i in range(s[0])]))
