#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class rectangle with two private instance variables"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """String representation of rectangle"""
        recStr = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                recStr += "#"
            if i < self.__height - 1 and self.__width != 0:
                recStr += "\n"
        return recStr

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
