#!/usr/bin/python3
""" new class student"""


class Student:
    """new class student"""

    def __init__(self, first_name, last_name, age):
        """initialise student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
