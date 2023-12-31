#!/usr/bin/python3
"""
 function that returns True if the object is an instance of,
 or if the object is an instance of a class that inherited from,
 the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns:
    bool: True if `obj` is an instance of or a subclass of `a_class`;
    False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
