#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    return dir(obj) + [attr for attr in dir(obj) if callable(getattr(obj, attr))]
