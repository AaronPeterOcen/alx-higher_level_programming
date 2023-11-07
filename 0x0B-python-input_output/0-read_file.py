#!/usr/bin/python3
"""
a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """prints the contents in stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
