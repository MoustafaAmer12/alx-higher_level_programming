#!/usr/bin/python3
"""
A Module that defines a function to
deserialize a json file format into an object
"""
import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
