#!/usr/bin/python3
""" define the MagicClass """

import math


class MagicClass:
    """
    Attributes
    radius : rad value
    """

    def __init__(self, radius=0):
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
