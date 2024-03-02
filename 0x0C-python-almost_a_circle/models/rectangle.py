#!/usr/bin/python3
'''
    Class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''
        Rectangle class that inherits from
        Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            return private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            sets private attributes
        '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
            return private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            sets private attribute
        '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
            return private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            sets private atrribute
        '''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
            return private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):       
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
            returns the area of a rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            prints representation of triangle to stdout
        '''
        if self.width == 0 or self.height == 0:
            print("")
            return
        

        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwrgs):
        '''
            update arguement
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
    def to_dictionary(self):
        '''
            dict represntation
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")},
    
    def __str__(self)
        '''
            Overwrites the string method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width, self.height)
