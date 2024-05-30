#!/usr/bin/python3
"""
Module for the CustomObject class.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize and save the instance."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Serialization error:", e)
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from the provided filename."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Deserialization error:", e)
            return None
