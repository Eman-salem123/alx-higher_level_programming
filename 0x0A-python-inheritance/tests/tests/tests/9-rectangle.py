#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A string in the format '[Rectangle] width/height'.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height
