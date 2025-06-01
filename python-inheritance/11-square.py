#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with size and validate it."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation specific to Square."""
        return f"[Square] {self.__size}/{self.__size}"
