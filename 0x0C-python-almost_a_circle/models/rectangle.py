#!/usr/bin/python3
"""
new class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    new class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
