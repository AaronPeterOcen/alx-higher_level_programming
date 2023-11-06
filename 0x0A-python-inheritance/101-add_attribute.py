#!/usr/bin/python3

""" function that adds a new attribute to an object if its possible"""


def new_attr(obj, name, value):
    """
    adds a new attribute to an object if its possible

     Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__setattr__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
