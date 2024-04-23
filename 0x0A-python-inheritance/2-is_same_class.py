#!/usr/bin/python3
"""
A Module that checks whether an object is
of the same given calss"""


def is_same_class(obj, a_class):
    """A function that checks whether an object is
    if the same given calss"""
    return type(obj) is a_class
