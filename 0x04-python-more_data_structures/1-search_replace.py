#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list.pop(search - 1)
    new_list.insert(search - 1, replace)
    return new_list
