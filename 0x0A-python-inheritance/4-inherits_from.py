#!/usr/bin/python3
"""
A Module that defines a function to check whether
an object is a child of a specified class
"""


def inherits_from(obj, a_class):
    """
    Returns:
        True of the obj is a child of the given class
    """
    return isinstance(obj, a_class) and not (type(obj) is a_class)
