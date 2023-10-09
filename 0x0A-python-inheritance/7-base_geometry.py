#!/usr/bin/python3
"""A module that contains the definition of the class BaseGeometry."""


class BaseGeometry:
    """definition of the BaseGeometry class.

    Attributes:


    Methods:
        area(self)
        integer_validator(self, name, value)
    """

    def area(self):
        """A function that raises an exception

        Raises:
            Exception: always with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validate 'value'.

        Args:
            name: name attached to the value.
            value (int): a positive integer value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
