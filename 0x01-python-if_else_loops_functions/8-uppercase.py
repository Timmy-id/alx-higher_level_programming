#!/usr/bin/python3
def uppercase(str):
    str_lst = []
    for letter in str:
        str_lst.append(letter.capitalize())
    new_str = "".join(str_lst)
    print("{:s}".format(new_str))
