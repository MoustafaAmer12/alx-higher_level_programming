#!/usr/bin/python3
"""A Module defining a function that
adds new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """A function that checks if an object is able
    to have new attributes else raises TypeError
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
