#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with {:d}".format().

    Args:
        value: integer to print
    Return:
        TypeError or ValueError on failure
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
