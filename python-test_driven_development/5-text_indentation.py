#!/usr/bin/python3
"""Task 5"""


def text_indentation(text):
    """prints text with 2 new lines afetr ".", "?", :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
        
    symbols = [".", "?", ":"]
    new_str = ""
    for i in range(len(text)):
        if text[i] == " " and flag == True:
            continue
        flag = False
        new_str += text[i]
        if text[i] in symbols:
            new_str += "\n" + "\n"
            flag = True
    print(new_str, end="")

