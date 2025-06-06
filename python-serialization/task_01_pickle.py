#!/usr/bin/env python3
"""Module for serializing and deserializing a custom object using pickle."""

import pickle


class CustomObject:
    """A class representing a custom object."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (pickle.PickleError, OSError):
            pass  # Optionally log error or print message

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return a CustomObject from a file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject or None: The deserialized object, or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except (pickle.PickleError, OSError, EOFError):
            pass
        return None
