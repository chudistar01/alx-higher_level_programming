#!/usr/bin/python3
"""Function that checks for subclass"""


def inherits_from(obj, a_class):
    """ object is an instance of inheited class.
    obj: object
    a_class: class
    returns None
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
