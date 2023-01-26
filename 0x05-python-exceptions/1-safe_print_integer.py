#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError:
        print("{} is not an integer".format(value))
        return False


print(safe_print_integer("School"))