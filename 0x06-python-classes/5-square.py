#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
