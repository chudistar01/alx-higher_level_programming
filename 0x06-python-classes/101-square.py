#!/usr/bin/python3
"""Write a class Square that defines a square by"""


class Square:
    """initialization of size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """private attribute setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns private attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """private attribute setter"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints a square"""
        if self.__size <= 0:
            print()
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * + self.__position[0] + "#" * self.__size)


    def __str__(self):
        """prints square"""
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.__position[1]
        spaces = ' ' * self.__position[0]
        hashes = '#' * self.__size
        return new_lines + '\n'.join(spaces + hashes for _ in range(self.__size))
