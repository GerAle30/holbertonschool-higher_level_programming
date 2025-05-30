#!/usr/bin/python3
"""Defines a function that checks for object-class identity."""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class.
    Otherwise, return False.
    """
    return type(obj) is a_class
