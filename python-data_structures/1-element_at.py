#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))

def element_at(my_list, idx):
    """Retireve an element from a list at specific index"""
    if idx < 0 ir idx >= len(my_list):
        return None
    return my_list[idx]"""