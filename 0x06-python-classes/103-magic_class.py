#!/usr/bin/python3
"""Magic Class Module"""
import math


class MagicClass:
    """Identifies a Circle"""
    def __init__(self, radius):
        """Initializes the Circle with a given radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculates the areaa of the circle
        Returns:
            Area"""
        return (self.__radius**2) * math.pi

    def circumference(self):
        """Calculates the circumference
        Returns:
            circumference"""
        return 2 * math.pi * self.__radius
