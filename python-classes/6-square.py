#!/usr/bin/python3
"""This module defines a class called Square
"""


class Square:
    """
    MyClass Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: Private instance attribute defaults to zero.
        Raises:
            TypeError: must be int
            ValueError: must be greater than zero
        """

        self.size = size
        self.position = position

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
            return
        for _ in range(self.__position[1]):
            print()
            if self.__position[1] > 0:
                pass
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
