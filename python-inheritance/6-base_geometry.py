#!/usr/bin/python3
"""Defines a base class for geometry."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
