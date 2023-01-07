#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for letter in str:
        new_str.append(letter.capitalize())
    return print("".join(new_str))
