#!/usr/bin/env python3
"""Implements mixins for swimming and flying behavior and a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming capability."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly using mixins."""

    def roar(self):
        """Prints dragon roar."""
        print("The dragon roars!")
