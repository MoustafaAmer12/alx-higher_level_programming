#!/usr/bin/python3
"""A Module defining a function that
adds new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
