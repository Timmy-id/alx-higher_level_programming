#!/usr/bin/python3
"""Class magic_class definition"""

import math


class MagicClass:
    """Class sMagicClass with a private instance variable
        The radius variable must be a number
    """

    def __init__(self, radius=0):
        """Initialize MagicClass with a private
            instance variable radius of 0
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the perimeter of the circle"""
        return 2 * math.pi * self.__radius
