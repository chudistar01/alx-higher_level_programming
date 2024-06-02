#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Represent a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a new rectangle.
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """class method
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:
            TypeError: either rect_1 or rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of rectangle"""
        return (self.__height + self.__width) * 2

    def __str__(self):
        """prints the string representation
        of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol) * self.width)
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """string representation that can be evaluated"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes function"""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
