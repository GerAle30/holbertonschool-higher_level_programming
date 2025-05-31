#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle inheritance"""

    def __init__(self, size):
        """Initialize the square using Rectangle's validator"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
