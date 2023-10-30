#!/usr/bin/python3
""" class that defines a rectangle """

class Rectangle:
    """
    Defines the Rectangel class
    Attributes:
    width: ...
    height: ...
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):

