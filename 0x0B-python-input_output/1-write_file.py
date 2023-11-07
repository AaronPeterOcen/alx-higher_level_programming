#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """wrtites a string to a txt file"""
    with open(filename, "w") as f:
        return f.write(text)
