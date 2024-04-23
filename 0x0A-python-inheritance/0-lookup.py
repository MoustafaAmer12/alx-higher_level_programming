#!/usr/bin/python3
"""A Module that defines a function that returns the attributes of a class
"""


def lookup(obj):
    """A Function that returns the attributes of an object
    Returns:
        List of attributes of object"""
    return list(type(obj).__dict__.keys())
