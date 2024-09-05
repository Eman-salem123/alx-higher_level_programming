#!/usr/bin/python3
""" 7-base_geometry module """


class BaseGeometry:

    """
    A base class for geometric shapes.

    This class provides common functionality and properties
    that are shared among different geometric shapes.
    Subclasses are expected to implement specific methods
    for their respective shapes.

    Attributes:
    None

    """

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
    Validate an integer value for a given name.

    This method checks whether the provided value is
    an integer and greater than zero.
    If the value fails any of these checks, it raises
    a TypeError or ValueError accordingly.

    Args:
        name (str): The name of the value being validated.
        value: The value to be validated.

    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is not greater than zero.

    Returns:
        None
    """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
