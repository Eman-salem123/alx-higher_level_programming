#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
                Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        The string includes the object's ID, coordinates (x, y), width,
        and height.

        Returns:
            str: A string representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def checker(self, name_atr, atr, hewi=True):
        """
        Check the validity of an attribute value.

        Args:
            name_atr (str): The name of the attribute being checked.
            atr (int): The value of the attribute being checked.
            hewi (bool, optional): Flag indicating whether the attribute
            must be greater than zero. Defaults to True.

        Raises:
            TypeError: If the attribute is not an integer.
            ValueError: If the attribute is not valid based on
            the specified conditions.

        Returns:
            None
        """
        if not isinstance(atr, int):
            raise TypeError(f"{name_atr} must be an integer")
        else:
            if hewi:
                if atr <= 0:
                    raise ValueError(f"{name_atr} must be > 0")
            if not hewi:
                if atr < 0:
                    raise ValueError(f"{name_atr} must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle by printing '#' characters in
        the shape of the rectangle.
        """
        for f in range(self.y):
            print()
        for i in range(self.height):
            for a in range(self.x):
                print(" ", end="")
            for e in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.

        Args:
            *args: Variable length argument list containing the new values
                   for the attributes in the following order: id, width,
                   height, x, y.
            **kwargs: Keyword arguments containing the new values for the
                      attributes. The attribute names should be used as the
                      keyword arguments.

        Returns:
            None
        """
        args_name = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(args_name):
                setattr(self, args_name[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle instance.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        Args:
            width (int): The new width of the rectangle.
        """
        self.checker("width", width, True)
        self.__width = width

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Args:
            height (int): The new height of the rectangle.
        """
        self.checker("height", height, True)
        self.__height = height

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            x (int): The new x-coordinate of the rectangle's position.

        Returns:
            None
        """
        self.checker("x", x, False)
        self.__x = x

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            y (int): The new y-coordinate of the rectangle's position.
        """
        self.checker("y", y, False)
        self.__y = y
