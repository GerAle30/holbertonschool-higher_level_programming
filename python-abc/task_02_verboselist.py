#!/usr/bin/env python3
"""Defines the VerboseList class that extends list with notifications."""


class VerboseList(list):
    """Custom list class that prints messages on mutations."""

    def append(self, item):
        """Append item and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Print message and remove item from the list."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print message and pop item from the list."""
        item = self[index]  # May raise IndexError if out of bounds
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
