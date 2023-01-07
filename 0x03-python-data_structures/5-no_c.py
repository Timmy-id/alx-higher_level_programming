#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for letter in new_string:
        if letter != 'c' and letter != 'C':
            return "".join(new_string)
        return "".join(new_string)
