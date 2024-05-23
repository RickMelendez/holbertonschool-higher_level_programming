#!/usr/bin/python3
"""
    BaseGeometry.
    """


class BaseGeometry:
    def area(self):
        """
        Method to calculate the area, to be implemented in subclasses
            """
        raise Exception(area() is not implemented)

    def integer_validator(self, name, value):
        """
        Method to validate if a value is an integer and greater than 0
            """
        if value != 1:
            raise TypeError()
        elif value <= 0:
            raise ValueError()
