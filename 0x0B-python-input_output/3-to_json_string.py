#!/usr/bin/python3
"""
A Module that creates a function to serialize
an object into a json string
"""
import json


def to_json_string(my_obj):
    """A Function that serializes an object
    into a JSON string
    Returns:
        JSON serialization of a string
    """
    return json.dumps(my_obj)
