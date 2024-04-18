#!/usr/bin/python3
"""
Module that adds two integers
add_integer:
    adds two given integers as params
"""


def add_integer(a, b=98):
    """Adds two integers
    Returns:
        sum of two integers"""
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if a < 0:
        a = ceil(a)
    if b < 0:
        b = ceil(b)
    return int(a) + int(b)
