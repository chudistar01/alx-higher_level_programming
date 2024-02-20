#!/usr/bin/python3
"""class checking function"""


def is_same_class(obj, a_class):
    """checks if an object is instance of a given class.
    Args:
    obj(any): object to check.
    a_class(type): class to match.
    Returns:
        if obj is exactly an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
