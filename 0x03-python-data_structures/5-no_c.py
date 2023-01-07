#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    new_string = list(my_string)
    for letter in new_string:
        if letter != 'c' and letter != 'C':
            new_list.append(letter)
    return "".join(new_list)
