#!/usr/bin/python3
"""This module defines a class called Square
"""


class Square:
    """
    MyClass Square
    """

    def __init__(self, size=0):
        """
        Args:
            size: Private instance attribute defaults to zero.
        Raises:
            TypeError: must be int
            ValueError: must be greater than zero
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates area
            Returns: value of area
        """

        return self.__size * 2

    @property
    def size(self):
        """
        Retrieve size
        Return: value of area
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        set size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
