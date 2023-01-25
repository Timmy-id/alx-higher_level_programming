#!/usr/bin/python3
"""Class square definition"""


class Square:
    """Class square with a private instance variable
        The size variable must be an integer and be greater than 0
    """

    def __init__(self, size=0):
        """Initialize square with a private instance variable size of 0"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def area(self):
        """Get the area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        return self.area == other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __le__(self, other):
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area

    def __lt__(self, other):
        return self.area < other.area

    def __ne__(self, other):
        return self.area != other.area
