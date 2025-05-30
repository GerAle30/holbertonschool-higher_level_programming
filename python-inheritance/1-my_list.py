#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""

class Mylist(list):
    """Custom list class that adds a print_sorted method."""
    
    def print_dorted(self):
        """Prints the list insorted (ascending)
        order without modyifying the original
        list"""
        print(sorted(self))
