#!/usr/bin/python3
"""
Module that creates a class with only valid instance attribute
first_name otherwise the instance attribute can't be created
"""


class LockedClass:
    """
    A class that only enables setting first_name attribute
    to instances
    """
    __slots__ = ["first_name"]
