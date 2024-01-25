#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function that deletes keys with a
    specific value in a dictionary"""
    if value not in a_dictionary.values():
        return a_dictionary

    updated_dictionary = {key: value for key, val in a_dictionary.items() if val != value)
