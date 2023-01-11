#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    sort_by_keys = {item: a_dictionary[item] for item in dict_keys}
    return sort_by_keys
