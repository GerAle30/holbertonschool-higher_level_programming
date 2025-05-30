#!/usr/bin/python3
"""Module for MyList class."""

class Mylist(list):
    """A subclass of list with a method to print the list sorted."""
    
    def print_dorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
