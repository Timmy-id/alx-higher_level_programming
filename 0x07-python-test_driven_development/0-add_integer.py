#!/usr/bin/python3
"""A function definition that adds two integers
    The two integers must be integers
    and the return value must be an integer also
    A TypeError should be returned if a different type is inputed
"""


def add_integer(a, b=98):
    """Function returns addition of a and b
            :param a: int :param b: int
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
