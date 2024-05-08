#!/usr/bin/python3
"""Write a class Square that defines a square by:"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initializes the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)
