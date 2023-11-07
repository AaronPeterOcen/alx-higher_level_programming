#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Intialize a new square.

        Args:
            size (int): The size of the new square.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
