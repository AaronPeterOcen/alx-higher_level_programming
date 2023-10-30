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
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
