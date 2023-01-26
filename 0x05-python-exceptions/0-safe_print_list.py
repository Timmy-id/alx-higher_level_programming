#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x == 0:
            for i in my_list:
                return ("{}".format(i))
        sliced_list = my_list[0:x]
        for i in sliced_list:
            return ("{}".format(i))
    except Exception:
        pass

print(safe_print_list([1,2,3,4,5], 2))