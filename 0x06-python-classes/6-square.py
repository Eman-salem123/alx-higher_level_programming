#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """

    def __init__(self, size=0, position=(0, 0)):
        """ init """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):

        a = isinstance(value, int)
        if a:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, values):

        if (not isinstance(values, tuple) or
                len(values) != 2 or
                not all(isinstance(num, int) for num in values) or
                not all(num >= 0 for num in values)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = values

    def area(self):
        """ area method """
        return (self.__size*self.__size)

    def my_print(self):
        """ print method """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for a in range(self.__size):
            print("".join(" " for k in range(self.__position[0])), end="")
            print("".join("#" for z in range(self.__size)))
