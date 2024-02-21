#!/usr/bin/python3
"""Defines file writing function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8).

    Args:
        filename (str): the name of the file
        text (str): text to write a file
    Returns:
        The number of charactes written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
