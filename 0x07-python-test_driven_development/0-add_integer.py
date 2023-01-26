#!/usr/bin/python3
"""A function definition that adds two integers"""


def add_integer(a, b=98):
    """Function returns addition of a and b
            :param a: int
            :param b: int
            :return: int
        If function arguments are not integers,
        TypeError is raised.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
