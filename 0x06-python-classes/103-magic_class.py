#!/usr/bin/python3
from math import pi

"""Class magic_class definition"""


class MagicClass():
    """Class sMagicClass with a private instance variable
        The radius variable must be a number
    """

    def __init__(self, radius=0):
        """Initialize MagicClass with a private
            instance variable radius of 0
        """
        if not isinstance(radius, int) or not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return self.__radius ** 2 * 2 * pi

    def circumference(self):
        """Calculate the perimeter of the circle"""
        return self.__radius * 2 * pi
