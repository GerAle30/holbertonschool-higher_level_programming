#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry validation"""

    def __init__(self, width, height):
        """Initialize a validated rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
