#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    i = 0
    for letter in str:
        if i != n:
            copy += letter
        i += 1
    return copy
