#!/usr/bin/python3
"""Empty BaseGeometry class"""


class BaseGeometry:
    """
    adding a public instance

    def __init__(self, name):
        self.name = name
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
