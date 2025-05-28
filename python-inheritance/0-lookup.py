#!/usr/bin/python3
"""This module defines a function to look up the methods"""
def lookup(obj):
    """ 
    Returns a list of attributes adn methods of an object
    
    Args:
    obj: The object to inspect.
    
    Returns:
    A list containing the names of the object's attribute and methods."""
    return dir(obj)