#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    print(dict_keys)
    new_dict = {item: a_dictionary[item] * 2 for item in dict_keys}
    print(new_dict)
    print(a_dictionary)
    return new_dict
