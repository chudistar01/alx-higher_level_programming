#!/usr/bin/python3
"""a function that returns True if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified class;
otherwise False"""


def is_kind_of_class(obj, a_class):
    """ function: is_kind_class
    obj: object
    a_class: class
    Returns: Bool
    """
    if isinstance(obj, a_class):
        return True
    return False
