#!/usr/bin/python3
"""Defines a function that checks inheritance relationships."""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or inherits from,
    the specified class. Otherwise, return False.
    """
    return isinstance(obj, a_class)
