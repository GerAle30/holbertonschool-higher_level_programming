#!/usr/bin/python3
"""Defines a class Square with size and position for printing."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size: The size of the square.
            position: A tuple of 2 positive integers representing position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, considering position."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each line of the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
