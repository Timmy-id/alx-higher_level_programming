#!/usr/bin/python3
"""Class square definition"""


class Square:
    """Class square with a private instance variable
        The size variable must be an integer and be greater than 0
    """

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            if len(value) != 2 and not (num >= 0 for num in value):
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        self.__postion = value

    def __init__(self, size=0):
        """Initialize square with a private instance variable size of 0"""
        self.size = size

    def area(self):
        """Get the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print(self.__size * "#", end="")
            print("")
