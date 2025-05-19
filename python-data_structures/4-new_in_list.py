#!/usr/bin/python3
def new_list(my_list, idx, element):
    """Creates a copy of the list and replace
     an element at a specific position"""
    new_list = my_list[:]

    if 0 <= idx < len(my_list):
        new_list[idx] = element

        return new_list
