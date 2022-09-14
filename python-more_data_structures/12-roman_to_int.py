#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1,
                'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    length = len(roman_string)
    for i in range(length):
        if i == length - 1:
            result += rom_dict[roman_string[i]]
        else:
            if rom_dict[roman_string[i]] >= rom_dict[roman_string[i + 1]]:
                result += rom_dict[roman_string[i]]
            else:
                result -= rom_dict[roman_string[i]]
    return result
