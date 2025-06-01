#!/usr/bin/env python3
"""Example of multiple inheritance with Fish, Bird, and FlyingFish classes."""


class Fish:
    """Represents a generic fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Represents a generic bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish with behaviors of both a fish and a bird."""

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat description."""
        print("The flying fish lives both in water and the sky!")
