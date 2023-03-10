#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class rectangle with two private instance variables"""

    # Class variable that counts the number of Rectangle instances
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        # When a Rectangle is created, the number_of_instances increases by 1
        Rectangle.number_of_instances += 1

    def __str__(self):
        """String representation of rectangle"""
        recStr = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                recStr += f"{self.print_symbol}"
            if i < self.__height - 1 and self.__width != 0:
                recStr += "\n"
        return recStr

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete an instance of the Rectangle"""
        print("Bye rectangle...")
        # When a Rectangle instance is deleted, the
        # number_of_instances decreases by 1
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def area(self):
        """Get the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
