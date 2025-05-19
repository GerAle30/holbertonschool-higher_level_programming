#!/usr/bin/python3
def print_matric_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    if matrix == [[]]:
        print()
        return

    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end="")
