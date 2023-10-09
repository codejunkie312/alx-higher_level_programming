#!/usr/bin/python3
"""A module that contains the definition of the class BaseGeometry."""


class BaseGeometry:
    """definition of the BaseGeometry class.

    Attributes:


    Methods:
    """

    def area(self):
        """A function that raises an exception

        Raises:
            Exception: always with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
