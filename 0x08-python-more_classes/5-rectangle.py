#!/usr/bin/python3
""" rectangle module """


class Rectangle:
    """ rectangle class """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height*self.__width

    def perimeter(self):
        if self.__height <= 0 or self.__width <= 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height <= 0 or self.__width <= 0:
            return ("")

        rect = []
        for a in range(self.__height):
            for e in range(self.__width):
                rect.append("#")
            if a != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        print("Bye rectangle...")
