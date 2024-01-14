#!/usr/bin/python3
"""
    wrting the first class base
"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string method
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """
        load from file
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        create method
        """
        from models.rectangle import Rectangle
        from models.square import Square

        #     # if cls.__name__ == "Rectangle":
        #     #     mod = Rectangle(1, 1)
        #     # elif cls.__name__ == "Square":
        #     #     mod = Square(1)
        #     # mod.update(**dictionary)
        #     # return mod

        if cls.__name__ == "Rectangle":
            return Rectangle(1, 1, 0, 0, **dictionary)
        elif cls.__name__ == "Square":
            return Square(1, 0, 0, **dictionary)
        else:
            return None
