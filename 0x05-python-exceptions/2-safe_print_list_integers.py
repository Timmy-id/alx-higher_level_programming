#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    sliced_list = my_list[0:x]
    for i in sliced_list:
        try:
            print("{:d}".format(i), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return count
