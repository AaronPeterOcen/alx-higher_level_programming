#!/usr/bin/python3
""" new class student"""
import json


class Student:
    """new class student"""

    def __init__(self, first_name, last_name, age):
        """initialise student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, my_list):
        """new method to_json"""
        return json.dumps(my_list)
