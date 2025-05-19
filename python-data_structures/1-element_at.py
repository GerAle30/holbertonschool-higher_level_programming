#!/usr/bin/python3
"""
Retrieve an element from a list at a specific index.

Args:
    my_list (list): The list to search
    idx (int): The index to retrieve

    returns:
        The element at the specified index or None if index is ot of range"""

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
