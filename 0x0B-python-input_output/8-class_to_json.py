#!/usr/bin/python3
"""function that returns the dictionary"""


def class_to_json(obj):
    """returns dict representation of an obj"""
    return obj.__dict__
