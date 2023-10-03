#!/usr/bin/python3
"""A module that contains a class that prevents the user from dynamically
creating new instance attributes, except if the new instance attribute is
called first_name.
"""


class LockedClass:
    """This is the LockedClass class definition."""
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """A function that initializes an instance of the LockedClass class.

        Args:
            first_name (str): The first name of the instance. (default: "")
        """
        self.first_name = first_name

    def __setattr__(self, name, value):
        """A function that sets an attribute of an instance of the LockedClass
        class.

        Args:
            name (str): The name of the attribute to set.
            value (str): The value to set the attribute to.

        Raises:
            AttributeError: If the attribute to set is not called first_name.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")
