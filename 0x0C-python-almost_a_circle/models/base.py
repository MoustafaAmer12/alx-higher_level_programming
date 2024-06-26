#!/usr/bin/python3
"""
Module that defines a base class for the
project initialization
"""
import json
import csv
import turtle


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
        """Converts list of dictionaries into JSON string
        Returns:
            JSON format string of `list_dictionaries`, or '[]' if None or
                empty
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
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

    @classmethod
    def create(cls, **dictionary):
        """A function that creates an object with the
        assigned attributes to the dict from its base type
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances read from a file
        """
        filename = f"{cls.__name__}.json"
        obj_list = []
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                data = file.readlines()
                inst_list = cls.from_json_string(data[0])
                for instance in inst_list:
                    obj = cls.create(**instance)
                    obj_list.append(obj)
        except FileNotFoundError:
            obj_list = []
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves Objects into a csv file
        """
        if cls.__name__ == "Rectangle":
            fields = ("id", "width", "height", "x", "y")
        elif cls.__name__ == "Square":
            fields = ("id", "size", "x", "y")
        filename = f"{cls.__name__}.csv"
        list_dict = []
        for item in list_objs:
            list_dict.append(item.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """Loads data from a csv file
        """
        if cls.__name__ == "Rectangle":
            fields = ("id", "width", "height", "x", "y")
        if cls.__name__ == "Square":
            fields = ("id", "size", "x", "y")
        filename = f"{cls.__name__}.csv"
        inst_list = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = csv.DictReader(file)
                for row in data:
                    for key in fields:
                        row[key] = int(row[key])
                    inst_list.append(cls.create(**row))
        except FileNotFoundError:
            return inst_list
        return inst_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws a list of shapes either squares
        or rectangles
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares
        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
        window.exitonclick()
