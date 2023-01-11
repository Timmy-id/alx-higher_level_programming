#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    sort_by_keys = {item: a_dictionary[item] for item in dict_keys}
    for item, val in sort_by_keys.items():
        print(f"{item}: {val}")
    return sort_by_keys
