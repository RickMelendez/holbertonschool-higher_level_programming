#!/usr/bin/python3
"""This module defines a class called Square"""


class Square:
    """Class Square"""
    
    def __init__(self, size):
        """Args:
        size: no type/value verification
        """
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
