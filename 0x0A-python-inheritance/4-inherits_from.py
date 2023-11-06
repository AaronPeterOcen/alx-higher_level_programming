#!/usr/bin/python3
"""
Determines whether the specified object is an instance of,
or if the object is an instance of a class that inherited from,
the given class.
"""


def inherits_from(obj, a_class):
    """
    Returns:
    bool: True if `obj` is an instance of a subclass of `a_class`;
    False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
