#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    remove_key = a_dictionary.pop(key, None)
    if remove_key is None:
        return a_dictionary
    return a_dictionary
