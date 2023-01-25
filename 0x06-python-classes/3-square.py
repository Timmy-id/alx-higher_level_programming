#!/usr/bin/python3
"""Class square definition"""


class Square:
    """Class square with a private instance variable
        The size variable must be an integer and be greater than 0
    """

    def __init__(self, size=0):
        """Initialize square with a private instance variable size of 0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the area of the square"""
        return self.__size * self.__size
