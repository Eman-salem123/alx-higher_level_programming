#!/usr/bin/python3
""" this module contain Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance
        with the given size.
    """

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        The string representation includes the size of the square.

        Returns:
            str: A string representation of the Square object.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
