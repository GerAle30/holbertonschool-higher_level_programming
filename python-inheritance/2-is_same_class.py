#!/bin/python3
"""
this module defines a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class Otherwise, returns False.

    Args:
        obj: The object to check
        a_class: The class to compare with

        Return:
            bool: True if obj is excatly an instance of a_class, otherwise False.
            """
            return type(obj) is a_class
