#!/usr/bin/python3
"""
A Module that returns the attributes
of an object in the form of JSON serializable object
"""


def class_to_json(obj):
    """A function that returns the dictionary
    of attributes of an object.
    """
    return obj.__dict__
