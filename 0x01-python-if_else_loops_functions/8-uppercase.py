#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for letter in str:
        new_str.append(letter.capitalize())
    print("".join(new_str), end="\n")
