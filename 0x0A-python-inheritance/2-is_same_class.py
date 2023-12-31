#!/usr/bin/python3
"""
function that returns True if
the object is exactly an instance of the specified class ;
otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns a list object"""
    if not isinstance(obj, a_class):
        return False

    if type(obj) == a_class:
        return True

    return False
