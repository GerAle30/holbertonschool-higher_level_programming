#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initialize a new square.
        
        Args:
            size (int): The size of the new square.
        
        Raises:
        TypeError: If size is not an integer.
        ValueEror: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size        