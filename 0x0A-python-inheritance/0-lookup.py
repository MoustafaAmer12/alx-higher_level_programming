#!/usr/bin/python3
"""A Module that defines a function that returns the attributes of a class
"""


def lookup(obj):
    return list(type(obj).__dict__.keys())
