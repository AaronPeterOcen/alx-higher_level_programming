#!/usr/bin/python3
""" class that inherits from int"""


class MyInt(int):

    """inverts == and != operators"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
