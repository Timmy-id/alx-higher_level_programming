#!/usr/bin/python3
def roman_to_int(roman_string):
    is_str = isinstance(roman_string, str)
    is_none = isinstance(roman_string, type(None))
    if is_str is False and is_none is False:
        return 0
    roman_and_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if len(roman_string) == 1:
        return roman_and_int.get(roman_string)
    return "Working"


print(roman_to_int("V"))
