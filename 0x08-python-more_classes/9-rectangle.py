#!/usr/bin/python3
"""
Module that identifies a Rectangle class
class:
    Rectangle
"""


class Rectangle:
    """
    A class that initializes rectangles
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Called upon creation of a new rectangle object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
        """
        return 0 if self.width == 0 or self.height == 0\
                    else 2 * (self.width + self.height)

    def __str__(self):
        """Called upon creating a str of an object
        Returns:
            str representation of the rectangle in the form of print symbols
        """
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Called upon creating a repr of an object
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Called upon deleting an object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method the compares two rectangles based on
        the area
        Returns:
            The biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        a_1 = rect_1.area()
        a_2 = rect_2.area()
        if a_1 >= a_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that creates a square instance of the Rectangle object
        """
        new_rect = cls(size, size)
        return new_rect
