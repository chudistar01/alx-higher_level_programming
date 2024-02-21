#!/usr/bin/python3
"""Defines file appending function"""


def write_file(filename="", text=""):
    """function that appends a string to a text file (UTF8).

    Args:
        filename (str): the name of the file
        text (str): text to append to a file
    Returns:
        The number of charactes appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
