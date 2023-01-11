#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    new_dict = {item: a_dictionary[item] * 2 for item in dict_keys}
    return new_dict
