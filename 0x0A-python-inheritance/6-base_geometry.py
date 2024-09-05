#!/usr/bin/python3
""" 5-base_geometry module """


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
        """
    Calculate the area of the geometric shape.

    This method calculates the area of the geometric shape.
    Since it's a placeholder method
    and not implemented in this base class,
    it raises an Exception to indicate that it needs
    to be implemented in subclasses.

    Raises:
        Exception: This method is not implemented in 
        the base class and must be overridden
                   in subclasses.

    Returns:
        None
    """
        raise Exception("area() is not implemented")
