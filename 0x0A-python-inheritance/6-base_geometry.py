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
