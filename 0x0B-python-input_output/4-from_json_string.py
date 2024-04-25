#!/usr/bin/python3
"""
A Module that deserializes a JSON
string object into the actual object
"""
import json


def from_json_string(my_str):
    """A Function that deserializes a JSON
    string to its original object
    Returns:
        Object after deserialization
    """
    return json.loads(my_str)
