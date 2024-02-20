#!/usr/bin/python3
"""function that adds a new attribute
to an object if it’s possible"""


def add_attribute(obj, att, value):
    """Add a new attribute to object.
    Args:
        obj(any): object.
        att: attribute name.
        value: value of attribute.
    Raises:
        TypeError: if attr is not added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
