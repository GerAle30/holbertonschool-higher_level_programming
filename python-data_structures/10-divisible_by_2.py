#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    if not my_list:
        return []

    result = []
    for i in my_list:
        result.append(i % 2 == 0)
    return result
