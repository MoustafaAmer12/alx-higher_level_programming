#!/usr/bin/python3
"""
Module that defines a base class for the
project initialization
"""
import json


class Base:
    """Base Class

    Description:
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes and
        to avoid duplicating the same code by extension, same bugs.

    Attrs:
        private class attribute: __nb_objects
        public instance attribute: id

    Methods:
        __init__: defines calss constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json representation of a
        list of dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representaion of an object
        into a file
        """
        filename = f"{cls.__name__}.json"
        json_list = []
        for obj in list_objs:
            json_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(cls.to_json_string(json_list), file)
