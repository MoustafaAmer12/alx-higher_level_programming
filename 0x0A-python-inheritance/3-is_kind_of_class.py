#!/usr/bin/python3
"""
A Module that checks whether an object is a kind of another
"""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True if the object is a kind of the class
    """
    return isinstance(obj, a_class)
