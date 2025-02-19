#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    """initialization of size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """returns size private attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """private attribute setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)
