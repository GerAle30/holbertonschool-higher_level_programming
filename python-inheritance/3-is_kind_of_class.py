#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of a class or a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified clas,,
    or if the object is an instance of a subclass of the specified class.

    Args:
        obj: The object to checks.
        a_class: The class to compare with

        Returns:
            bool: True if obj is an  instance of a_class or subclass of a_class, False otherwise.
            """
            return isinstance(obj, a_class)
