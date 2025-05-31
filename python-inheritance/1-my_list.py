#!/usr/bin/python3
"""This module defines the MyList class that inherits from list."""


class MyList(list):
    """Custom list class that adds a print_sorted method."""

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order
        without modifying the original list.
        """
        print(sorted(self))
