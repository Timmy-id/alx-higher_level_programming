#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_reverse = my_list.reverse()
    for num in list_reverse:
        print("{:d}".format(num))
