#!/usr/bin/python3
"""Defines a class Square with getter and setter for size."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size: The size of the square (default is 0).
        """
        self.size = size  # usamos el setter aquí

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value: The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2