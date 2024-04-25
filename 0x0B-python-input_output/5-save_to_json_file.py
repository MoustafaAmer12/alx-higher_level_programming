#!/usr/bin/python3
"""
A Module that defines a function
to write the JSON representation of an
object into a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes the json
    serialization of an object into a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
