#!/usr/bin/python3
""" a class Square that defines a square based on 1-square.py """


class Square:
    """
    Attributes:
    size : square size
    """

    def __init__(self, size=0):
        """defines new square
        Args: size=0: square size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
