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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representaion of an object
        into a file
        """
        filename = f"{cls.__name__}.json"
        json_list = []
        if not list_objs:
            list_objs = []
        for obj in list_objs:
            json_list.append(obj.to_dictionary())
        json_dict = cls.to_json_string(json_list)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """A function that deserializes a JSON
        string into a dict"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
