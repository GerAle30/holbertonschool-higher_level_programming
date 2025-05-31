#!/usr/bin/python3
"""Defines a function to check for strict class inheritance."""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class.
    Return False if obj is an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
