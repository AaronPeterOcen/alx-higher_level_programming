#!/usr/bin/python3
"""
    wrting the first class base
"""
import json


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string method
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file method
        """
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))
