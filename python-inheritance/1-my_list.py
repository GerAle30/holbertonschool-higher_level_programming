#!/usr/bin/python3


"""
this module defines a class my list
that inherits from list and adds a method to
print the list sorted in ascending order"""


class mylist(list):

    """MyList is a subclass of the built-in list class
    Adds a method to print the list in sorted order"""

    def print_sorted(self):
        """ Prints the list in sorted (ascending) order
        order without modifying the original list"""
        print(sorted(self))
